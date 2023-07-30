using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;
using TMPro;

public class NotificationButton : MonoBehaviour
{
    private string Sender, Time, Content;
    private ButtonConfigHelper buttonConfig;
    private Interactable interactable;
    public TextMeshPro TxtTime, TxtContent;
    public GameObject bgPanel;
    public MeshRenderer NameTag, IconTag;
    private const float animationLength = 0.5f;
    private float panelMaxHeight = 0.022f;
    private AudioSource audioSource;
    public AudioClip notificationClip;

    private void OnEnable()
    {
        if (!buttonConfig)
        {
            buttonConfig = GetComponent<ButtonConfigHelper>();
            
        }
        if (!interactable)
        {
            interactable = GetComponent<Interactable>();
        }
        if (!audioSource)
        {
            audioSource = GetComponent<AudioSource>();
        }

        ToggleNotificationUI(false);
        //panelMaxHeight = bgPanel.transform.localScale.y;
        bgPanel.transform.localScale = new Vector3(bgPanel.transform.localScale.x, 0f, bgPanel.transform.localScale.z);
        
        buttonConfig.MainLabelText = Sender;
        buttonConfig.SetQuadIconByName(Sender);
        TxtTime.text = Time;
        TxtContent.text = Content;
        audioSource.PlayOneShot(notificationClip, 1f);
        StartCoroutine(DisplayNotificationAnimation());
    }

    IEnumerator DisplayNotificationAnimation()
    {
        float timer = 0f;
        while (timer < animationLength)
        {
            timer += UnityEngine.Time.deltaTime;
            timer = Mathf.Clamp(timer, 0, animationLength);
            bgPanel.transform.localScale = new Vector3(bgPanel.transform.localScale.x, panelMaxHeight * timer/animationLength, bgPanel.transform.localScale.z);
            bgPanel.transform.localPosition = new Vector3(bgPanel.transform.localPosition.x, 0.5f * panelMaxHeight * (1 - timer / animationLength), bgPanel.transform.localPosition.z);
            yield return new WaitForEndOfFrame();
        }
        ToggleNotificationUI(true);
    }

    void ToggleNotificationUI(bool toggleOn)
    {
        interactable.IsEnabled = toggleOn;
        TxtTime.gameObject.SetActive(toggleOn);
        TxtContent.gameObject.SetActive(toggleOn);
        NameTag.enabled = toggleOn;
        IconTag.enabled = toggleOn;
    }


    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    public void UpdateValues(string sender, string time, string content)
    {
        Sender = sender;
        Time = time;
        Content = content;
    }
}
