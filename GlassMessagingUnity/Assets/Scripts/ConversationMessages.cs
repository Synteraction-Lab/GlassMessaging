using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;

public class ConversationMessages : MonoBehaviour
{
    //Summary
    public string conversationId;
    private int currentTier = 0;
    private int lastReadMessageCount = 0;
    private ScrollingObjectCollection scrollView;


    private void OnEnable()
    {
        if(scrollView == null)
        {
            scrollView = GetComponentInParent<ScrollingObjectCollection>();
        }
        scrollView.ResetMaintainOffset();
        scrollView.MoveToIndex(currentTier, false);
    }

    private void OnDisable()
    {
        for(int i = lastReadMessageCount; i < transform.childCount; i++)
        {
            MessageText msgUI = transform.GetChild(i).GetComponent<MessageText>();
            if(msgUI.Sender != "Me")
            {
                msgUI.SetMessageStatus(MessageText.MessageStatus.READ);
            }
        }
        lastReadMessageCount = transform.childCount;
        currentTier = scrollView.FirstVisibleCellIndex;
    }
}
