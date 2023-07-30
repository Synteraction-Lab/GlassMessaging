using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

using Microsoft.MixedReality.Toolkit.UI;
using Microsoft.MixedReality.Toolkit.Input;
using TMPro;
using Microsoft.MixedReality.Toolkit;
using Microsoft.MixedReality.Toolkit.Physics;

public class RingMouseHandler : MonoBehaviour
{ 
    public ScrollingObjectCollection messageScrollView;
    public Interactable keyboard, voice, send;
    public GameObject keyboardOutline, voiceOutline, sendOutline;
    private Interactable currentActiveInteractable;
    public UIController uiController;
    public int scrollingSpeed = 3;
    public GameObject touchActivationBound;
    public float keyHoldTimer = 0.5f;

    private float timerUpKey = 0f;

    private float timerLeftKey = 0f;
   
    // See KeyCodes: https://docs.unity3d.com/Packages/com.unity.tiny@0.13/rt/tiny_runtime/enums/_runtimefull_.ut.core2d.keycode.html

    private const KeyCode SCROLL_UP_ACTION_KEYCODE = KeyCode.PageUp;
    private const KeyCode SCROLL_DOWN_ACTION_KEYCODE = KeyCode.PageDown;
    private const KeyCode SCROLL_LEFT_ACTION_KEYCODE = KeyCode.F5;
    private const KeyCode SCROLL_RIGHT_ACTION_KEYCODE = KeyCode.Period;


    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        //// check keys codes
        //foreach (KeyCode kcode in System.Enum.GetValues(typeof(KeyCode)))
        //{
        //    if (Input.GetKey(kcode))
        //        Debug.Log("KeyCode down: " + kcode);
        //}

        // UP key

        if (Input.GetKeyDown(SCROLL_UP_ACTION_KEYCODE))
        {
            timerUpKey = 0f;
        }

        if (Input.GetKey(SCROLL_UP_ACTION_KEYCODE))
        {
            timerUpKey += Time.deltaTime;
            if (timerUpKey >= keyHoldTimer)
            {
                uiController.ConversationBackToTop();
            }
        }

        if (Input.GetKeyUp(SCROLL_UP_ACTION_KEYCODE))
        {
            Debug.Log("ScrollUp key pressed");
            
            if(timerUpKey < keyHoldTimer)
            {
                uiController.ConversationMouseCommand(false);
            }
        }


        // DOWN key

        if (Input.GetKeyUp(SCROLL_DOWN_ACTION_KEYCODE))
        {
            Debug.Log("ScrollDown key pressed");
            uiController.ConversationMouseCommand(true);
        }


        // LEFT key

        if (Input.GetKeyDown(SCROLL_LEFT_ACTION_KEYCODE))
        {
            timerLeftKey = 0f;
        }

        if (Input.GetKey(SCROLL_LEFT_ACTION_KEYCODE))
        {
            timerLeftKey += Time.deltaTime;
        }


        if (Input.GetKeyUp(SCROLL_LEFT_ACTION_KEYCODE))
        {
            Debug.Log("ScrollLeft key pressed");

            if (timerLeftKey < keyHoldTimer)
            {
                ActivateCurrentFunctionButton();
                if (keyboard == currentActiveInteractable)
                {
                    uiController.ActivateKeyboard();
                }
            }
            else
            {
                bool isUIVisible = uiController.IsUIVisible();
                isUIVisible = !isUIVisible;
                uiController.SetUIVisible(isUIVisible);
            }
        }

        //if (Input.GetKeyDown(SCROLL_LEFT_ACTION_KEYCODE))
        //{
        //    Debug.Log("ScrollLeft key pressed");
        //    ActivateCurrentFunctionButton();
        //}
        //if (Input.GetKeyUp(SCROLL_LEFT_ACTION_KEYCODE))
        //{
        //    if (currentActiveInteractable == keyboard)
        //    {
        //        uiController.ActivateKeyboard();
        //    }
        //}


        // RIGHT key

        if (Input.GetKeyDown(SCROLL_RIGHT_ACTION_KEYCODE))
        {
            Debug.Log("ScrollRight key pressed");
            ChangeActiveFunctionButton();
        }

    }

    void ActivateCurrentFunctionButton()
    {
        if(currentActiveInteractable != null)
        {
            if(currentActiveInteractable == send && !send.gameObject.activeInHierarchy)
            {
                currentActiveInteractable = null;
                return;
            }

            currentActiveInteractable.TriggerOnClick(true);
        }
    }

    void ChangeActiveFunctionButton()
    {
        if (keyboard.gameObject.activeInHierarchy)
        {
            if(currentActiveInteractable == null)
            {
                touchActivationBound.SetActive(true);
                SetSelectionOutline(keyboardOutline);
                currentActiveInteractable = keyboard;
                return;
            }

            if (currentActiveInteractable == keyboard)
            {
                SetSelectionOutline(voiceOutline);
                currentActiveInteractable = voice;
                return;
            } 

            if(currentActiveInteractable == voice)
            {
                if (send.gameObject.activeInHierarchy)
                {
                    SetSelectionOutline(sendOutline);
                    currentActiveInteractable = send;
                } else
                {
                    SetSelectionOutline(keyboardOutline);
                    currentActiveInteractable = keyboard;
                }
                return;
            }

            if(currentActiveInteractable == send)
            {
                SetSelectionOutline(keyboardOutline);
                currentActiveInteractable = keyboard;
                return;
            }

           
        }
    }

    void SetSelectionOutline (GameObject outlineObject)
    {
        keyboardOutline.SetActive(false);
        voiceOutline.SetActive(false);
        sendOutline.SetActive(false);
        outlineObject.SetActive(true);
    }

    public void SetCurrentSelectionToNull()
    {
        currentActiveInteractable = null;
        keyboardOutline.SetActive(false);
        voiceOutline.SetActive(false);
        sendOutline.SetActive(false);
    }

}