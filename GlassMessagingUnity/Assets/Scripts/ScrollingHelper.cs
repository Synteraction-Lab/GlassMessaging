using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;

public class ScrollingHelper : MonoBehaviour
{
    private ScrollingObjectCollection scrollView;
    // Start is called before the first frame update
    void Start()
    {
        scrollView = GetComponent<ScrollingObjectCollection>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void MoveToTier(int tier)
    {
        scrollView.MoveToIndex(tier);
    }

    public void MoveToBottom()
    {
        scrollView.MoveToIndex(1000);
    }
}
