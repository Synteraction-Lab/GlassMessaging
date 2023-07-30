using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Microsoft.MixedReality.Toolkit.Rendering;
using TMPro;
using UnityEditor;

public class MessageText : MonoBehaviour
{
    public GameObject ParentElement;
    public GameObject Panel;
    //public TMPro.TMP_Text TxtSender;
    public TMPro.TMP_Text TxtTime;
    public TMPro.TMP_Text TxtContent;

    private bool valuesUpdated = false;

    public string Sender { get; set; }
    public string Time { get; set; }
    public string Content { get; set; }

    private const float basePanelSize = 0.033f;
    private const float basePanelCornerRadius = 0.23f;
    private const float baseContentYPos = 0f;

    private const float deltaContentYPos = 0f;
    private const float deltaPanelSize = 0.008f;

    private const float baseTimeYPos = -0.0167f;
    private const float deltaTimeYPos = 0.004f;

    public Color readMessageColor, unreadMessageColor, ownMessageColor;
    public enum MessageStatus
    {
        OWN,
        READ,
        UNREAD
    }

    private MessageStatus currentMessageStatus;


    [HideInInspector] public float offset;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (valuesUpdated)
        {
            //if (TxtSender != null)
            //{
            //    TxtSender.text = Sender;
            //}
            if (TxtTime != null)
            {
                TxtTime.text = Time;
            }
            if (TxtContent != null)
            {
                TxtContent.text = Content;
            }

            ResizePanel();
            valuesUpdated = false;
            //StartCoroutine(DelayedResizePanel());
        }
    }



    public void SetMessageStatus(MessageStatus messageStatus)
    {
        currentMessageStatus = messageStatus;
        MaterialInstance instancedMaterial = Panel.GetComponent<MaterialInstance>();
        switch (currentMessageStatus) {
            case MessageStatus.OWN:
                instancedMaterial.Material.SetColor("_Color", ownMessageColor);
                instancedMaterial.Material.SetFloat("_InnerGlow", 0f);
                break;
            case MessageStatus.READ:
                instancedMaterial.Material.SetColor("_Color", readMessageColor);
                instancedMaterial.Material.SetFloat("_InnerGlow", 0f);
                break;
            case MessageStatus.UNREAD:
                instancedMaterial.Material.SetColor("_Color", unreadMessageColor);
                instancedMaterial.Material.SetFloat("_InnerGlow", 1f);
                break;
            default:
                return;
        }
    }

    public void UpdateValues(string sender, string time, string content)
    {
        Sender = sender;
        Time = time;
        Content = content;

        valuesUpdated = true;
    }

    private IEnumerator DelayedResizePanel()
    {
        yield return new WaitForEndOfFrame();

        ResizePanel();
    }

    private void ResizePanel()
    {
        //Canvas.ForceUpdateCanvases();
        int deltaLineNumber = (int) (TxtContent.GetComponent<TextMeshPro>().preferredHeight / 0.015f) - 2;
        Debug.Log(TxtContent.GetComponent<TextMeshPro>().preferredHeight + "; " + deltaLineNumber);
        Vector3 contentPos = TxtContent.rectTransform.localPosition;
        TxtContent.rectTransform.localPosition = new Vector3(contentPos.x, baseContentYPos - deltaContentYPos * deltaLineNumber - deltaPanelSize / 2f * deltaLineNumber, contentPos.z);
        Vector3 timePos = TxtTime.rectTransform.localPosition;
        TxtTime.rectTransform.localPosition = new Vector3(timePos.x, baseTimeYPos - deltaTimeYPos * deltaLineNumber - deltaPanelSize / 2f * deltaLineNumber, timePos.z);

        Panel.transform.localScale = new Vector3(Panel.transform.localScale.x, basePanelSize + deltaPanelSize * deltaLineNumber, Panel.transform.localScale.z);
        Panel.transform.localPosition = new Vector3(Panel.transform.localPosition.x, -deltaPanelSize / 2f * deltaLineNumber, Panel.transform.localPosition.z);

        Panel.GetComponent<MaterialInstance>().AcquireMaterial().SetFloat("_RoundCornerRadius", basePanelCornerRadius * basePanelSize / Panel.transform.localScale.y);

        offset = deltaPanelSize * deltaLineNumber;
    }

    public void ResetValues()
    {
        UpdateValues(null, null, null);
    }

    public void Show()
    {
        ParentElement.SetActive(true);
    }

    public void Hide()
    {
        ParentElement.SetActive(false);
    }

    public void ChangeOpacity(float newOpacity)
    {
        float opacity = Mathf.Clamp01(newOpacity); 
        //Color newColor = Panel.GetComponent<MaterialInstance>().Material.GetColor("_Color");
        //Debug.Log("Color [old]:" + newColor);
        Color baseColor = readMessageColor;
        if (currentMessageStatus == MessageStatus.UNREAD)
        {
            baseColor = unreadMessageColor;
        } else if (currentMessageStatus == MessageStatus.OWN)
        {
            baseColor = ownMessageColor;
        }
        
        //Debug.Log("ChangeOpacity New:" + opacity);
        //Debug.Log("Color [new]:" + newColor);
        Color newColor = baseColor * opacity;
        newColor.a = 1f;
        Panel.GetComponent<MaterialInstance>().Material.SetColor("_Color", newColor);
    }
}
