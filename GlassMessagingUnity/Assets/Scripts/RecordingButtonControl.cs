using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;
//using Microsoft.MixedReality.Toolkit.Experimental.UI;
using Microsoft.MixedReality.Toolkit.Input;

[RequireComponent(typeof(Interactable))]
public class RecordingButtonControl : MonoBehaviour
{
    //test
    private Interactable interactable;
    public DictationHandler dictationHandler;
    public GameObject inputObject;
    //public MRTKTMPInputField inputField;
    private bool listening;
    public AudioClip recording_start, recording_stop;
    private AudioSource audioSource;
    // Start is called before the first frame update
    void Start()
    {
        if(dictationHandler == null)
        {
            Debug.LogError("Please assign dictation handler to record button!");
        }
        interactable = GetComponent<Interactable>();
        audioSource = GetComponent<AudioSource>();
        interactable.IsToggled = false;
        listening = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (dictationHandler.IsListening != listening)
        {
            listening = dictationHandler.IsListening;
            interactable.IsToggled = listening;
            audioSource.PlayOneShot(listening ? recording_start : recording_stop, 0.6f);
        }
        if(dictationHandler.IsListening && (!inputObject.activeInHierarchy))
        {
            inputObject.SetActive(true);
        }
    }

    public void ButtonClicked()
    {
        if (dictationHandler.IsListening)
        {
            dictationHandler.StopRecording();
        } else
        {
            dictationHandler.StartRecording();
        }
    }

    public void StopDictation()
    {
        if (dictationHandler.IsListening)
        {
            dictationHandler.StopRecording();
        }
    }

    public void StartDictation()
    {
        if (!dictationHandler.IsListening)
        {
            dictationHandler.StartRecording();
        }
    }
}
