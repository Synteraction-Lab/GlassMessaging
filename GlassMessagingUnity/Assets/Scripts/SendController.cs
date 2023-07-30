using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using Microsoft.MixedReality.Toolkit.Experimental.UI;
using Microsoft.MixedReality.Toolkit.UI;

public class SendController : MonoBehaviour
{
    public ChatData chatData;
    public ChatCommunication chatCommunicator;

    public bool enableSentSound = true;
    public AudioClip messageSentAudio;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

    }

    public void SendNewChatMessage(MRTKTMPInputField textInputField)
    {
        if (!textInputField.gameObject.activeInHierarchy)
            return;

        Debug.Log("SendNewChatMessage: " + ((textInputField != null) ? textInputField.text : "null"));
        if (chatData == null || chatCommunicator == null || textInputField == null || textInputField.text.Equals(""))
        {
            Debug.LogError("Empty elements");
            return;
        }

        string messageContent = DictationCorrector.GetCleanedText(textInputField.text);

        Message message = new Message();
        message.conversation_id = chatData.GetCurrentConversationId();
        message.sender = chatData.GetUser();
        message.time = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds();
        message.content = messageContent;
        message.read = true;

        chatCommunicator.SendMessage(message);
        
        textInputField.text = "";

        if (enableSentSound)
        {
            AudioSource audioSource = GetComponentInParent<AudioSource>();
            audioSource.PlayOneShot(messageSentAudio, 0.5f);
        }        
    }

  
}
