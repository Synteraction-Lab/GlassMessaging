using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Microsoft.MixedReality.Toolkit.Utilities.Solvers;
using Microsoft.MixedReality.Toolkit.Experimental.UI;

[RequireComponent(typeof(SolverHandler))]
public class SolverControl : MonoBehaviour
{
    private SolverHandler handler;
    public float additionalXRotation = 6f;
    private Follow followSolver;
    public MRTKTMPInputField inputField;
    public Camera camera;
    private List<Vector3> cameraPositionSamples = new List<Vector3>();
    public float walkSpeed;

    public bool enableDynamicFollowSwitch;
    // Start is called before the first frame update
    void Start()
    {
        handler = GetComponent<SolverHandler>();
        followSolver = GetComponent<Follow>();
        followSolver.enabled = true;
        handler.AdditionalRotation = Vector3.right * additionalXRotation;
        if (enableDynamicFollowSwitch)
        {
            StartCoroutine(CalculateCameraMovement());
        }
        else
        {
            SolverToMovement();
        }
    }

    // Update is called once per frame
    void Update()
    {
        followSolver.IgnoreReferencePitchAndRoll = ( inputField.gameObject.activeInHierarchy && inputField.IsKeyboardActive() );
    }

    IEnumerator CalculateCameraMovement()
    {
        while (true)
        {
            
            if (cameraPositionSamples.Count < 5) {
                cameraPositionSamples.Add(camera.transform.position);
            } else
            {
                cameraPositionSamples.RemoveAt(0);
                cameraPositionSamples.Add(camera.transform.position);
                float avgCamSpeed = (cameraPositionSamples[4] - cameraPositionSamples[0]).magnitude / 1.0f;
                //Debug.Log("Average Cam Speed: "+avgCamSpeed);
                if(avgCamSpeed > walkSpeed)
                {
                    SolverToMovement();
                } else
                {
                    SolverToStationary();
                }
            }
            yield return new WaitForSeconds(0.2f);
        }
    }

    void SolverToStationary()
    {
        followSolver.MoveLerpTime = 0.3f;
        followSolver.RotateLerpTime = 0.3f;
        followSolver.MaxViewHorizontalDegrees = 10f;
        followSolver.MaxViewVerticalDegrees = 10f;
    }

    // see https://learn.microsoft.com/en-us/dotnet/api/microsoft.mixedreality.toolkit.experimental.utilities.follow
    void SolverToMovement()
    {
        followSolver.MoveLerpTime = 0.1f; // 0.15f
        followSolver.RotateLerpTime = 0.15f; //0.1f
        followSolver.MaxViewHorizontalDegrees = 0.5f; // 0.1f
        followSolver.MaxViewVerticalDegrees = 0.5f;//0f
    }

}
