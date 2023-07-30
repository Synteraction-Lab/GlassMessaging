using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;
using Microsoft.MixedReality.Toolkit.Experimental.UI;
using Microsoft.MixedReality.Toolkit.Input;

public class UIController : MonoBehaviour
{
    public ChatData chatData;
    public GameObject parentUI;

    public ScrollingObjectCollection convoScrollView;
    public ScrollingHelper convoScrollingHelper;
    public ScrollingObjectCollection messageScrollView;
    public ScrollingHelper messageScrollingHelper;
    public GameObject keyboardAndVoice;

    public Transform conversationParent;
    public Transform contactParent;
    public Transform convoMessageParent;
    public GameObject messageTemplateObject;

    public const int MAX_CHARACTERS_LAST_MESSAGE = 15;

    private ConversationMessages currentConvoMessage;
    public Vector3 initialUIPosition;
    public float messageOffset = 0.035f;

    private List<ConversationButton> _conversationUIList = new List<ConversationButton>();
    private List<ConversationButton> _contactUIList = new List<ConversationButton>();
    private List<ConversationMessages> _conversationMessagesUIList = new List<ConversationMessages>();

    private List<Conversation> _currentSortedConvos = new List<Conversation>();

    private ConversationButton activeConversation;

    public NotificationButton notificationButton;
    public float notificationLifetime = 8f;
    private bool notificationActive = false;
    private Coroutine notificationCoroutine;
    private string currentNotificationSenderName;

    public InstructionMessage instructionMessage;

    public MRTKTMPInputField keyboardInput;
    public RecordingButtonControl voiceDictationInput;

    public float OpacityOfMessageHighest = 0.60f;
    public float OpacityOfMessageLowest = 0.45f;
    public float OpacityGradietStep = 0.02f;

    private bool isUIVisible = true;

    // Start is called before the first frame update
    void Start()
    {
        // Assumption: conversationUIList and contactUIList have same number fixed elements
        //PointerUtils.SetHandRayPointerBehavior(PointerBehavior.AlwaysOff);
        PointerUtils.SetGazePointerBehavior(PointerBehavior.AlwaysOff);
        //https://docs.microsoft.com/en-us/windows/mixed-reality/mrtk-unity/mrtk2/architecture/controllers-pointers-and-focus?view=mrtkunity-2022-05


        foreach (ConversationButton conversation in conversationParent.GetComponentsInChildren<ConversationButton>())
            _conversationUIList.Add(conversation);

        foreach (ConversationButton contact in contactParent.GetComponentsInChildren<ConversationButton>())
            _contactUIList.Add(contact);

        foreach (ConversationMessages convoMessage in convoMessageParent.GetComponentsInChildren<ConversationMessages>())
        {
            _conversationMessagesUIList.Add(convoMessage);
            convoMessage.gameObject.SetActive(false);
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (chatData.IsDataUpdated())
        {
            UpdateConversationElements(chatData, _conversationUIList, "Recency");
            //UpdateConversationElements(chatData, _contactUIList, "Alphabet");
            UpdateMessageElements(chatData, _conversationMessagesUIList);
            UpdateInstructionElement(chatData, instructionMessage);
            chatData.SetDataUpdated(false);

            // disable notification if the notification is related to the selected chat
            if (notificationActive && activeConversation != null && activeConversation.ConversationName == currentNotificationSenderName)
            {
                notificationActive = false;
            }
        }


        if (!chatData.IsNotificationQueueEmpty() && !notificationActive)
        {
            if(notificationCoroutine != null)
            {
                StopCoroutine(notificationCoroutine);
                notificationButton.gameObject.SetActive(false);
                currentNotificationSenderName = null;
            }
            // FIXME: set UI visible upon new instruction
            if (!IsUIVisible())
            {
                SetUIVisible(true);
            }

            notificationCoroutine = StartCoroutine(DisplayNotification());          
        }

    }

    IEnumerator DisplayNotification()
    {
        notificationActive = true;
        Message msg = chatData.GetLastMessageFromNotificationQueue();
        notificationButton.UpdateValues(msg.sender, GetFormattedTimeString(msg.time), msg.content);
        currentNotificationSenderName = msg.sender;
        notificationButton.gameObject.SetActive(true);
        float timer = 0f;
        while (notificationActive && timer < notificationLifetime)
        {
            yield return new WaitForEndOfFrame();
            timer += Time.deltaTime;
        }
        notificationActive = false;
        notificationButton.gameObject.SetActive(false);
        currentNotificationSenderName = null;
    }

    public void DestroyNotification()
    {
        if (notificationActive)
        {
            // enable UI if it's not visible
            if (!isUIVisible)
            {
                SetUIVisible(true);
            }

            ConversationVoiceCommand(currentNotificationSenderName);
            notificationActive = false;
        } 
    }

    public void ConversationClicked(ConversationButton clickedChat)
    {
        string clickedConversationId = clickedChat.ConversationId;
        Debug.Log("Clicked ConversationId: " + clickedConversationId);
        chatData.SetCurrentConversationId(clickedConversationId);
        activeConversation = clickedChat;

        // FIXME: change the unread counts
        chatData.MarkConversationRead(clickedConversationId);

        if (!keyboardAndVoice.activeInHierarchy)
        {
            keyboardAndVoice.SetActive(true);
            convoScrollView.TiersPerPage = 3;
            convoScrollView.UpdateContent();
        }

        ToggleClickedConversation(clickedChat, _conversationUIList);
    }

    private void ToggleClickedConversation(ConversationButton clickedChat, List<ConversationButton> conversationUIElementList)
    {
        conversationUIElementList.ForEach(obj => obj.Toggle(false));
        clickedChat.Toggle(true);
    }

    public void ConversationMouseCommand(bool next)
    {
        if (activeConversation == null)
        {
            _conversationUIList[0].GetComponent<Interactable>().TriggerOnClick();
            convoScrollingHelper.MoveToTier(0);
        }
        else
        {
            int newIndex = _conversationUIList.IndexOf(activeConversation) + (next ? 1 : -1);
            if(newIndex >= _conversationUIList.Count - 1)
            {
                newIndex = _conversationUIList.Count - 1; // 0
            } 
            if(newIndex <= 0)
            {
                newIndex = 0; // _conversationUIList.Count - 1
            }
            _conversationUIList[newIndex].GetComponent<Interactable>().TriggerOnClick();
            convoScrollingHelper.MoveToTier(newIndex);
        }
    }

    public void ConversationVoiceCommand(string conversationName)
    {
        List<string> sortedNames = _currentSortedConvos.Select<Conversation, string>(convo => convo.name).ToList();
        int convoIndex = sortedNames.IndexOf(conversationName);
        if(convoIndex < 0)
        {
            Debug.LogError("Conversation Name Not Found!");
            return;
        }
        _conversationUIList[convoIndex].GetComponent<Interactable>().TriggerOnClick();
        convoScrollingHelper.MoveToTier(convoIndex);

    }

    public void ConversationReplyCommand(string conversationName)
    {
        ConversationVoiceCommand(conversationName);
        
    }

    public void ConversationBackToTop()
    {
        _conversationUIList[0].GetComponent<Interactable>().TriggerOnClick(true);
        convoScrollingHelper.MoveToTier(0);
    }

    private void UpdateConversationElements(ChatData chatDataObject, List<ConversationButton> conversationUIElementList, string sortingMethod)
    {
        List<Conversation> conversations = chatDataObject.GetConversations();
        String currentConversationId = chatData.GetCurrentConversationId();

        if (conversations.Count < conversationUIElementList.Count)
        {
            HideConversationElements(conversationUIElementList);
        }

        // FIXME: fix the proper way
        if (sortingMethod.Equals("Recency"))
        {
            UpdateConversationUIs(conversationUIElementList, GetSortedConversationsByRecency(conversations), currentConversationId);
        }
        else
        {
            UpdateConversationUIs(conversationUIElementList, GetSortedConversationsByAlphabet(conversations), currentConversationId);
        }
    }

    private void HideConversationElements(List<ConversationButton> conversationUIElementList)
    {
        conversationUIElementList.ForEach(obj => obj.Hide());
    }

    private List<Conversation> GetSortedConversationsByRecency(List<Conversation> fullConversationDataList)
    {
        // FIXME: sort by recency
        List<Conversation> clone = new List<Conversation>(fullConversationDataList);
        _currentSortedConvos = clone.OrderByDescending(x => GetLastMessageTime(x)).ToList();
        return _currentSortedConvos;
    }

    private List<Conversation> GetSortedConversationsByAlphabet(List<Conversation> fullConversationDataList)
    {
        // FIXME: sort by alphabet
        return fullConversationDataList;
    }

    // Note: both list MUST have equal size
    private void UpdateConversationUIs(List<ConversationButton> conversationUIElementList, List<Conversation> sortedConversationDataList, string currentConversationId)
    {
        int updatingElementCount = Math.Min(conversationUIElementList.Count, sortedConversationDataList.Count);

        for (int i = 0; i < updatingElementCount; i++)
        {
            ConversationButton conUI = conversationUIElementList.ElementAt(i);
            Conversation con = sortedConversationDataList.ElementAt(i);
            // string conversationId, string conversationName, string conversationIcon, string lastMessage, string unreadCount
            conUI.UpdateValues(con.id, con.name, con.icon, GetLastMessageString(con), GetUnreadCountString(con));
            conUI.Toggle(con.id == currentConversationId);
            conUI.Show();
        }
    }

    private Message GetLastMessage(Conversation conversation)
    {
        List<Message> messages = conversation.messages;

        if (messages == null || messages.Count == 0)
        {
            return null;
        }
        return messages.ElementAt(messages.Count - 1);
    }

    private long GetLastMessageTime(Conversation conversation)
    {
        Message lastMsg = GetLastMessage(conversation);
        if (lastMsg == null)
        {
            return 0;
        }
        return lastMsg.time;
    }

    private string GetLastMessageString(Conversation conversation)
    {
        Message lastMsg = GetLastMessage(conversation);
        if (lastMsg == null)
        {
            return string.Empty;
        }

        string lastMessageContent = lastMsg.content;
        return lastMessageContent.Substring(0, Math.Min(lastMessageContent.Length, MAX_CHARACTERS_LAST_MESSAGE));
    }

    private string GetUnreadCountString(Conversation conversation)
    {
        List<Message> messages = conversation.messages;

        if (messages == null || messages.Count == 0)
        {
            return string.Empty;
        }

        int unreadCount = messages.Where(s => s != null && !s.read).Count();
        if (unreadCount == 0)
        {
            return string.Empty;
        }
        
        return unreadCount.ToString();
    }

    private void UpdateReadMessage()
    {

    }

    private void UpdateMessageElements(ChatData chatDataObject, List<ConversationMessages> conversationMessagesUIList)
    {
        string currentConversationId = chatDataObject.GetCurrentConversationId();
        if (currentConversationId == null)
            return;

        List<Message> messages = chatDataObject.GetMessages(currentConversationId);

        if(currentConvoMessage == null || (currentConversationId != currentConvoMessage.conversationId))
        { 
            if (currentConvoMessage != null)
                currentConvoMessage.gameObject.SetActive(false);
            foreach(ConversationMessages convoMessage in conversationMessagesUIList)
            {
                if(convoMessage.conversationId == currentConversationId)
                {
                    currentConvoMessage = convoMessage;
                    convoMessage.gameObject.SetActive(true);
                    break;
                }
            }
        }


        StartCoroutine(UpdateMessageUIs(currentConvoMessage, messages));
    }

    private List<Message> GetSortedMessagesByRecency(List<Message> fullMessageDataList)
    {
        // FIXME: sort by recency (Does this duplicate data? maybe not as it may shallow copy)
        List<Message> clone = new List<Message>(fullMessageDataList);
        clone.Reverse();
        return clone;
    }

    private IEnumerator UpdateMessageUIs(ConversationMessages currentConvoMessage, List<Message> sortedMessageDataList)
    {
        int messageCount = currentConvoMessage.transform.childCount;
        bool addedNewMessages = messageCount < sortedMessageDataList.Count;

        for (int i = messageCount; i < sortedMessageDataList.Count; i++)
        {
            yield return new WaitForEndOfFrame();

            Message msg = sortedMessageDataList.ElementAt(i);

            GameObject messageUIObj = Instantiate(messageTemplateObject, currentConvoMessage.transform) as GameObject;
            MessageText msgUI = messageUIObj.GetComponent<MessageText>();

            // string sender, string time, string content
            msgUI.UpdateValues(msg.sender, GetFormattedTimeString(msg.time), msg.content);

            if(msg.sender == "Me")
            {
                msgUI.SetMessageStatus(MessageText.MessageStatus.OWN);
                
            } else
            {
                msgUI.SetMessageStatus(MessageText.MessageStatus.UNREAD);
            }
            //msgUI.Show();                        

            if (i == 0)
            {
                messageUIObj.transform.localPosition = initialUIPosition;
            }
            else
            {
                Transform prevMessageObj = currentConvoMessage.transform.GetChild(i - 1);
                messageUIObj.transform.localPosition = prevMessageObj.localPosition - Vector3.up * (prevMessageObj.GetComponent<MessageText>().offset + messageOffset);
            }
            

            yield return new WaitForEndOfFrame();
        }

        messageScrollView.UpdateContent();
        if(currentConvoMessage.transform.childCount > 3)
            messageScrollingHelper.MoveToBottom();

        if (addedNewMessages)
        {
            ChangeOpacityOfMessages(currentConvoMessage);
        }        
    }

    private void ChangeOpacityOfMessages(ConversationMessages currentConvoMessage)
    {
        int newMessageCount = currentConvoMessage.transform.childCount;
        for (int indexFromLatest = 0; indexFromLatest < newMessageCount; indexFromLatest++)
        {
            MessageText msgUIFromLatest = currentConvoMessage.transform.GetChild(newMessageCount - 1 - indexFromLatest).GetComponent<MessageText>();
            //Debug.Log("opacity: " + indexFromLatest + ": " + GetNewOpacity(indexFromLatest));
            msgUIFromLatest.ChangeOpacity(GetNewOpacity(indexFromLatest));
        }
    }

    private float GetNewOpacity(int indexFromLatest)
    {
        float newOpacity = OpacityOfMessageHighest - OpacityGradietStep * indexFromLatest;
        newOpacity = newOpacity < OpacityOfMessageLowest ? OpacityOfMessageLowest : newOpacity;
        return newOpacity;
    }

    private string GetFormattedTimeString(long timeInMillis)
    {
        DateTime dateTime = new DateTime(1970, 1, 1, 0, 0, 0, 0, DateTimeKind.Utc).AddMilliseconds(timeInMillis).ToLocalTime();
        return dateTime.ToString("hh:mm tt");
    }

    public void SetUIVisible(bool isVisible)
    {
        isUIVisible = isVisible; 

        if (isUIVisible)
        {
            parentUI.SetActive(true);
        }
        else
        {
            parentUI.SetActive(false);
        }
    }

    public bool IsUIVisible()
    {
        return isUIVisible;
    }


    public void ActivateKeyboard()
    {
        keyboardInput.ActivateInputField();
        //DeactivateVoiceDictation();
    }

    public void DeactviateKeyboard()
    {
        keyboardInput.DeactivateKeyboard();
    }

    private void UpdateInstructionElement(ChatData chatData, InstructionMessage instructionMessage)
    {
        string instruction = chatData.GetInstruction();
        instructionMessage.UpdateInstruction(instruction);

        // show or hide instrution based on the instruction content
        if (System.String.IsNullOrEmpty(instruction))
        {
            instructionMessage.Hide();
        }
        else
        {
            // FIXME: set UI visible upon new instruction
            if (!IsUIVisible())
            {
                SetUIVisible(true);
            }

            instructionMessage.Show();
            instructionMessage.PlayInstructionSound();
        }
    }

    public void ActivateVoiceDictation()
    {
        voiceDictationInput.StartDictation();
        DeactviateKeyboard();
    }

    public void DeactivateVoiceDictation()
    {
        voiceDictationInput.StopDictation();
    }
}
    
