using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using TMPro;
using Microsoft.MixedReality.Toolkit.UI;

public class ConversationButton : MonoBehaviour
{
    public GameObject ParentButton;
    public TMPro.TMP_Text TxtName;
    public TMPro.TMP_Text TxtUnreadCount;
    public TMPro.TMP_Text TxtLastMessage;

    private ButtonConfigHelper buttonConfigHelper;

    private bool valuesUpdated = false;

    public string ConversationId { get; set; }
    public string ConversationName { get; set; }
    public string ConversationIcon { get; set; }
    public string LastMessage { get; set; }
    public string UnreadCount { get; set; }

    // Start is called before the first frame update
    void Start()
    {
        buttonConfigHelper = ParentButton.GetComponent<ButtonConfigHelper>();
    }

    // Update is called once per frame
    void Update()
    {
        if (valuesUpdated)
        {
            if (TxtName != null)
            {
                TxtName.text = ConversationName;
            }
            if(TxtUnreadCount != null)
            {
                TxtUnreadCount.text = UnreadCount;
            }
            if(TxtLastMessage != null)
            {
                TxtLastMessage.text = LastMessage;
            }
            if (buttonConfigHelper != null)
            {
                buttonConfigHelper.SetQuadIconByName(ConversationIcon);
            }
        }
    }

    public void UpdateValues(string conversationId, string conversationName, string conversationIcon, string lastMessage, string unreadCount)
    {
        ConversationId = conversationId;
        ConversationName = conversationName;
        ConversationIcon = conversationIcon;
        LastMessage = lastMessage;
        UnreadCount = unreadCount;

        valuesUpdated = true;
    }

    public void ResetValues()
    {
        UpdateValues(null, null, null, null, null);
    }

    public void Show()
    {
        ParentButton.SetActive(true);
    }

    public void Hide()
    {
        ParentButton.SetActive(false);
    }

    public void Toggle(bool toggleOn)
    {
        ParentButton.GetComponent<Interactable>().IsToggled = toggleOn;
    }
}
