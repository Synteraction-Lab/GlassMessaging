using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

using Microsoft.MixedReality.Toolkit.Experimental.UI;
using Microsoft.MixedReality.Toolkit.UI;
using Microsoft.MixedReality.Toolkit.Input;

public class DictationCorrector : MonoBehaviour
{
    public DictationHandler dictationHandler;
    public Interactable sendButton;
    public MRTKTMPInputField textInputField;

    private const string SEND_COMMAND_LEFTOVER = "send.";

    private bool dictationActive = false;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (dictationHandler.IsListening != dictationActive)
        {
            dictationActive = dictationHandler.IsListening;
            if (!dictationActive)
            {
                processDictatedText();
            }
        }
    }


    private void processDictatedText()
    {
        if (textInputField == null || !textInputField.gameObject.activeInHierarchy || !sendButton.gameObject.activeInHierarchy)
        {
            return;
        }            

        string messageContent = GetCleanedText(textInputField.text);
        textInputField.text = messageContent;

        if (messageContent != null && messageContent.EndsWith(SEND_COMMAND_LEFTOVER))
        {
            messageContent = messageContent.Substring(0, messageContent.Length - SEND_COMMAND_LEFTOVER.Length);      

            textInputField.text = messageContent;
            sendButton.TriggerOnClick(true);
        }
    }

    public static string GetCleanedText(string text)
    {
        try
        {
            return getCorrectedText(text);
        }
        catch (Exception e)
        {
            Debug.LogError("Error in getCleanedText: " + e.ToString());
            return text;
        }
    }

    private static string getCorrectedText(string text)
    {
        if (text == null)
        {
            return null;
        }

        string trimmed = text.Trim();
        // remove extra "." 
        int end_char_location = trimmed.Length - 1;
        for (int i = end_char_location; i > 1; i--)
        {
            if (trimmed[i] == '.' && (trimmed[i - 1] == '.' || trimmed[i - 1] == '?' || trimmed[i - 1] == '!'))
            {
                trimmed = trimmed.Remove(i);
            }
            else
            {
                break;
            }
        }
        // remove extra " " or "." before "?"
        trimmed = trimmed.Trim();
        end_char_location = trimmed.Length - 1;
        for (int i = end_char_location; i > 1; i--)
        {
            if (trimmed[i] == '?' && (trimmed[i - 1] == '.' || trimmed[i - 1] == ' '))
            {
                trimmed = trimmed.Remove(i-1);
            }
            else
            {
                break;
            }
        }
     
        // make first letter upper
        if (trimmed.Length > 1)
        {
            // add "." if needed
            end_char_location = trimmed.Length - 1;
            if (trimmed[end_char_location] != '.' && trimmed[end_char_location] != '?')
            {
                trimmed = trimmed + ".";
            }

            trimmed = trimmed[0].ToString().ToUpper() + trimmed.Substring(1);
        }        

        return trimmed;
    }
}
