using Microsoft.MixedReality.Toolkit;
using Microsoft.MixedReality.Toolkit.Input;
using Microsoft.MixedReality.Toolkit.UI;
using UnityEngine;
using TMPro;
using UnityEngine.Events;

public class CommunicatorGestureHandler : MonoBehaviour, IMixedRealityGestureHandler<Vector3>
{
    public TextMeshPro debugText;
    [SerializeField]
    private MixedRealityInputAction manipulationAction = MixedRealityInputAction.None;
    //public UnityEvent onAirtapComplete;
    public Interactable sendController;
    private void OnEnable()
    {
        // Instruct Input System that we would like to receive all input events of type IMixedRealityGestureHandler
        CoreServices.InputSystem?.RegisterHandler<IMixedRealityGestureHandler>(this);
        debugText.text = "debug activated";
    }

    private void OnDisable()
    {
        // Instruct Input System to disregard all input events of type IMixedRealityGestureHandler
        CoreServices.InputSystem?.UnregisterHandler<IMixedRealityGestureHandler>(this);
    }

    public void OnGestureUpdated(InputEventData<Vector3> eventData)
    {
        
    }
    
    public void OnGestureCompleted(InputEventData<Vector3> eventData)
    {
        debugText.text = "Gesture completed: " + eventData.MixedRealityInputAction.Description;
        MixedRealityInputAction action = eventData.MixedRealityInputAction;
        if (action == manipulationAction)
        {
            if (sendController.gameObject.activeInHierarchy)
            {
                sendController.TriggerOnClick(true);
            }
        }
    }

    public void OnGestureStarted(InputEventData eventData)
    {
        debugText.text = "Gesture started: " + eventData.MixedRealityInputAction.Description;
    }

    public void OnGestureUpdated(InputEventData eventData)
    {

    }

    public void OnGestureCompleted(InputEventData eventData)
    {
        debugText.text = "Gesture completed: " + eventData.MixedRealityInputAction.Description;
        MixedRealityInputAction action = eventData.MixedRealityInputAction;
        if (action == manipulationAction)
        {
            if (sendController.gameObject.activeInHierarchy)
            {
                sendController.TriggerOnClick(true);
            }
        }
    }

    public void OnGestureCanceled(InputEventData eventData)
    {

    }
}
