using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;

namespace Microsoft.MixedReality.Toolkit.Input
{

    public class GridScrolling : BaseInputHandler, IMixedRealityInputActionHandler
    {

        private ScrollingObjectCollection scrollView = null;

        // Start is called before the first frame update
        void Start()
        {
            scrollView = GetComponentInParent<ScrollingObjectCollection>();
        }

        // Update is called once per frame
        void Update()
        {

        }

        private ScrollingObjectCollection GetParentScrollView()
        {
            return GetComponentInParent<ScrollingObjectCollection>();
        }

        private void ScrollUp()
        {
            Debug.Log("ScrollUp");
            scrollView.MoveByTiers(-1);
        }

        private void ScrollDown()
        {
            Debug.Log("ScrollDown");
            scrollView.MoveByTiers(1);
        }



        // A copy from InputActionHandler


        [SerializeField]
        [Tooltip("ScrollDown Action to handle")]
        private MixedRealityInputAction ScrollDownInputAction = MixedRealityInputAction.None;

        [SerializeField]
        [Tooltip("ScrollUp Action to handle")]
        private MixedRealityInputAction ScrollUpInputAction = MixedRealityInputAction.None;

        [SerializeField]
        [Tooltip("Whether input events should be marked as used after handling so other handlers in the same game object ignore them")]
        private bool MarkEventsAsUsed = false;


        #region InputSystemGlobalHandlerListener Implementation

        /// <inheritdoc />
        protected override void RegisterHandlers()
        {
            CoreServices.InputSystem?.RegisterHandler<IMixedRealityInputActionHandler>(this);
        }

        /// <inheritdoc />
        protected override void UnregisterHandlers()
        {
            CoreServices.InputSystem?.UnregisterHandler<IMixedRealityInputActionHandler>(this);
        }

        #endregion InputSystemGlobalHandlerListener Implementation

        void IMixedRealityInputActionHandler.OnActionStarted(BaseInputEventData eventData)
        {
            //if (eventData.MixedRealityInputAction == InputAction && !eventData.used)
            //{
            //    OnInputActionStarted.Invoke(eventData);
            //    if (MarkEventsAsUsed)
            //    {
            //        eventData.Use();
            //    }
            //}
        }
        void IMixedRealityInputActionHandler.OnActionEnded(BaseInputEventData eventData)
        {
            //Debug.Log("input: " + eventData.MixedRealityInputAction.Description + " : " + eventData.used);
            if (eventData.MixedRealityInputAction == ScrollDownInputAction && !eventData.used)
            {
                ScrollDown();
                if (MarkEventsAsUsed)
                {
                    eventData.Use();
                }
            }
            if (eventData.MixedRealityInputAction == ScrollUpInputAction && !eventData.used)
            {
                ScrollUp();
                if (MarkEventsAsUsed)
                {
                    eventData.Use();
                }
            }
        }


    }
}
