using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChatData : MonoBehaviour
{
    private static UserConversation userConversation = null; 

    private static string currentConversationId = null;
    private static string instruction = null;

    private static bool dataUpdated = false;

    private List<Message> messageNotificationQueue = new List<Message>();

    // Start is called before the first frame update
    void Start()
    {

        if (userConversation == null)
        {
            userConversation = new UserConversation();
            userConversation.user = "";
            userConversation.conversations = new List<Conversation>();

            SetDataUpdated(true);
        }

    }

    // Update is called once per frame
    void Update()
    {

    }

    public string GetUser()
    {
        return userConversation.user;
    }

    public List<Conversation> GetConversations()
    {
        return userConversation.conversations;
    }

    // return null if not found
    private Conversation GetConversationById(string conversationId)
    {
        return userConversation.conversations.FirstOrDefault(conversation => conversation.id == conversationId);
    }

    public List<Message> GetMessages(string conversationId)
    {
        Conversation existingConversation = GetConversationById(conversationId);

        if (existingConversation == null)
        {
            Debug.LogError("Failed to find conversation for id: " + conversationId);
            return new List<Message>();
        }

        return existingConversation.messages;
    }


    public bool MarkConversationRead(string conversationId)
    {
        List<Message> messages = GetMessages(conversationId);

        if (messages.Count == 0)
        {
            return false;
        }

        int lastUnreadMsgIndex = messages.Count - 1;
        while (lastUnreadMsgIndex >=0 && !messages.ElementAt(lastUnreadMsgIndex).read)
        {
            Message lastUnreadMsg = messages.ElementAt(lastUnreadMsgIndex);
            lastUnreadMsg.read = true;
            if (messageNotificationQueue.Contains(lastUnreadMsg))
            {
                messageNotificationQueue.Remove(lastUnreadMsg);
            }
            lastUnreadMsgIndex--;
        }

        return true;
    }

    public string GetCurrentConversationId()
    {
        return currentConversationId;
    }

    public void SetCurrentConversationId( string conversationId)
    {
        currentConversationId = conversationId;
        SetDataUpdated(true);
    }

    public void UpdateInstruction(string newInstruction)
    {
        Debug.Log("UpdateInstruction::" + newInstruction);
        instruction = newInstruction;
        SetDataUpdated(true);
    }

    public string GetInstruction()
    {
        return instruction;
    }

    public bool IsDataUpdated()
    {
        return dataUpdated;
    }

    public void SetDataUpdated(bool update)
    {
        dataUpdated = update;
    }

    public bool IsNotificationQueueEmpty()
    {
        return messageNotificationQueue.Count == 0;
    }

    public Message GetLastMessageFromNotificationQueue()
    {
        Message msg = messageNotificationQueue[0];
        messageNotificationQueue.RemoveAt(0);
        return msg;
    }

    public bool UpdateMessage(Message newMessage)
    {
        string messageConversationId = newMessage.conversation_id;

        Conversation existingConversation = GetConversationById(messageConversationId);

        if (existingConversation == null)
        {
            Debug.LogError("Failed to find conversation for id: " + messageConversationId);
            return false;
        }
       
        Debug.Log("UpdateMessage::" + newMessage.time + ": " + newMessage.content);
        existingConversation.messages.Add(newMessage);
        if(!newMessage.read)
            messageNotificationQueue.Add(newMessage);
        SetDataUpdated(true);
        
        return true;
    }

    public bool UpdateConversation(Conversation newConversation)
    {
        string conversationId = newConversation.id;
        Conversation existingConversation = userConversation.conversations.FirstOrDefault(conversation => conversation.id == conversationId);

        if (existingConversation != null)
        {
            Debug.LogError("Duplicate conversation entry for id: " + conversationId);
            return false;
        }

        Debug.Log("UpdateConversation::" + newConversation.id + ": " + newConversation.name);
        userConversation.conversations.Add(newConversation);
        SetDataUpdated(true);

        return true;
    }

    public bool UpdateUserConversation(UserConversation newUserConversation)
    {
        // FIXME: rewrite data
        Debug.Log("UpdateUserConversation::" + newUserConversation.user);
        userConversation = newUserConversation;
        currentConversationId = null;
        SetDataUpdated(true);

        return true;
    }
}





[System.Serializable]
public class UserConversation
{
    public string user;
    public List<Conversation> conversations;
}


[System.Serializable]
public class Conversation
{
    public string id;
    public string name;
    public string icon;
    public List<Message> messages;
}

[System.Serializable]
public class Message
{
    public string conversation_id;
    public string sender;
    public long time;
    public string content;
    public bool read;
}
