# GlassMessagingUnity
Unity project for the GlassMessagingUnity

## Requirements
- Unity2021.3.6f1 or higher

## Setup
- On first-time importing into Unity, choose ignore compilation error, and make the following changes to the code. 
  - Look for **WindowsDictationInputProvider.cs**. Change 392-408 to followings:
      - ```cs
        private void DictationRecognizer_DictationComplete(DictationCompletionCause cause){ 
            using (DictationCompletePerfMarker.Auto()){
                if(cause == DictationCompletionCause.TimeoutExceeded){
                    Microphone.End(deviceName);
                    dictationResult = textSoFar.ToString();
                    StopRecording();
                }
            Service?.RaiseDictationComplete(inputSource, dictationResult, dictationAudioClip);
            textSoFar = null;
            dictationResult = string.Empty;
            }
        }
    - This is to make the dictation time out recognized as complete, and keep the original dictation results. 
  - Look for **ScrollingObjectCollection.cs**. Add function ResetMaintainOffset() at line 1996:
    - ```cs
      public void ResetMaintainOffset(){
          ResetInteraction();
          UpdateContent();
      }
  - Look for MRTKTMPInputField.cs. Add several functions at line 34:
    - ```cs
      public bool IsKeyboardActive(){
          return !shouldHideSoftKeyboard && (m_SoftKeyboard != null) && m_SoftKeyboard.active;
      }
      
      public void ActivateKeyboard(){
          shouldHideSoftKeyboard = false;
          ActivateInputField();
      }
      
      public void DeactivateKeyboard(){
          DeactivateInputField();
          shouldHideSoftKeyboard = true;
      }

    
## Installation
- create a `communicator_config.json` file inside `Videos/Communicator` directory in HoloLens
- add the server address to the `communicator_config.json` as follows
	- ```javascript
		{
			"host":"<IP_ADDRESS>",
			"port":"8080"
		}
	  ```
	- NOTE: both the device (e.g., HoloLens2) and server computer should be connected via a PRIVATE network (e.g., phone hotspot)
- run the [GlassMessagingPython](../GlassMessagingPython) to create a socket connection

## Contact person
- [Nuwan Janaka](https://nuwanjanaka.info/) ([In](https://www.linkedin.com/in/nuwan-janaka/))
- [Peisen Xu](https://www.nus-hci.org/our-team/)