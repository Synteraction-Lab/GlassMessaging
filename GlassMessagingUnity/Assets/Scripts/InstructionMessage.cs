using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InstructionMessage : MonoBehaviour
{
    public GameObject ParentElement;
    public GameObject Panel;
    public TMPro.TMP_Text TxtInstruction;
    public AudioClip instructionAudio;

    private string instruction = null;
    private bool valuesUpdated = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (valuesUpdated)
        {
            if (TxtInstruction != null)
            {
                TxtInstruction.text = instruction;
            }

            valuesUpdated = false;
        }
        
    }

    public void UpdateInstruction(string newInstruction)
    {
        if (newInstruction != instruction)
        {
            instruction = newInstruction;
            valuesUpdated = true;
        }
    }

    public void Show()
    {
        ParentElement.SetActive(true);
    }

    public void Hide()
    {
        ParentElement.SetActive(false);
    }

    public void PlayInstructionSound()
    {
        AudioSource audioSource = ParentElement.GetComponent<AudioSource>();
        audioSource.PlayOneShot(instructionAudio, 0.5f);
    }
}
