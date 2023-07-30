using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading;
using UnityEngine;

#if !UNITY_EDITOR
using System.Threading.Tasks;
#endif


public static class Constants
{
    public const char CHAT_COMM_TYPE_SPERATOR = '|'; 

    public const string CHAT_TYPE_USER_CONVERSATION = "U";
    public const string CHAT_TYPE_CONVERSATION = "C";
    public const string CHAT_TYPE_MESSAGE = "M";
    public const string CHAT_TYPE_INSTRUCTION_MESSAGE = "I";
    public const string CHAT_TYPE_DUMMY = "D";

    public const string CHAT_PACKET_CHECK_CONNECTION =  CHAT_TYPE_DUMMY + "|"; 
}

// Orignal source: https://foxypanda.me/tcp-client-in-a-uwp-unity-app-on-hololens/
// Better implementation (?): https://github.com/endel/NativeWebSocket
public class ChatCommunication : MonoBehaviour
{
    public ConfigLoader configLoader = null;

    public bool AutoConnect = true;

    public ChatData chatData = null;


#if !UNITY_EDITOR
    private bool _useUWP = true;
    private Windows.Networking.Sockets.StreamSocket socket;
    private Task exchangeTask;
#endif

#if UNITY_EDITOR
private bool _useUWP = false;
System.Net.Sockets.TcpClient client;
System.Net.Sockets.NetworkStream stream;
private Thread exchangeThread;
#endif

    private Byte[] bytes = new Byte[256];
    private StreamWriter writer;
    private StreamReader reader;

    private bool exchanging = false;
    private bool exchangeStopRequested = false;
    private string lastTxPacket = null;

    private string errorStatus = null;
    private string successStatus = null;

    private bool connectionAttempted = false;

    // Start is called before the first frame update
    void Start()
    {

    }


    // Update is called once per frame
    void Update()
    {
        if (AutoConnect && !connectionAttempted && configLoader != null)
        {
            Connect(configLoader.GetHost(), configLoader.GetPort());
            connectionAttempted = true;
        }

        if (errorStatus != null)
        {           
            ProcessErrorStatus(errorStatus);
            errorStatus = null;
        }
        if (successStatus != null)
        {
            Debug.Log("Sucess:" + successStatus);
            successStatus = null;
        }
    }

    void OnDestroy()
    {
        StopExchange();
    }

    public void SendMessage(Message message)
    {
        string txData = Constants.CHAT_TYPE_MESSAGE + Constants.CHAT_COMM_TYPE_SPERATOR + JsonUtility.ToJson(message);
        if(chatData != null)
        {
            chatData.UpdateMessage(message);
        }
        lastTxPacket = txData;
    }

    private void ProcessErrorStatus(string status)
    {
        Debug.Log("Error:" + errorStatus);

        // restart after disconnection?
        if (AutoConnect && connectionAttempted)
        {
            StopExchange();
            connectionAttempted = false;
        }

    }


    private void ProcessReceivedData(string data)
    {
        //Debug.Log("Processing data:" + data);
        if (data == null)
        {
            Debug.LogError("Received a frame but data was null");
            return;
        }

        // data format: <TYPE> <TYPE_SEPERATOR> <JSON_STRING>
        string[] parts = data.Split(Constants.CHAT_COMM_TYPE_SPERATOR);

        if (parts.Length != 2)
        {
            Debug.LogError("Wrong data format: " + data);
            return;
        }

        string type = parts[0];
        string content = parts[1];

        switch (type)
        {
            case Constants.CHAT_TYPE_DUMMY:
                // DO NOTHING
                break;
            case Constants.CHAT_TYPE_MESSAGE:
                ProcessMessage(content);
                break;
            case Constants.CHAT_TYPE_INSTRUCTION_MESSAGE:
                ProcessInstuctionMessage(content);
                break;
            case Constants.CHAT_TYPE_CONVERSATION:
                ProcessConversation(content);
                break;
            case Constants.CHAT_TYPE_USER_CONVERSATION:
                ProcessUserConversation(content);
                break;
            default:
                Debug.LogError("Unknown type: " + type);
                break;
        }

        type = null;
        content = null;
        parts = null;

    }

    private void ProcessMessage(string jsonString)
    {
        try
        {
            Message message = JsonUtility.FromJson<Message>(jsonString);
            Debug.Log("New message");

            if (chatData != null)
            {
                chatData.UpdateMessage(message);
            }
            message = null;
        }
        catch
        {
            Debug.LogError("Failed to read message: " + jsonString);
        }
    }

    private void ProcessInstuctionMessage(string jsonString)
    {
        try
        {
            Message message = JsonUtility.FromJson<Message>(jsonString);
            Debug.Log("New instruction message");

            if (chatData != null)
            {
                chatData.UpdateInstruction(message.content);
            }
            message = null;
        }
        catch
        {
            Debug.LogError("Failed to read instruction message: " + jsonString);
        }
    }

    private void ProcessConversation(string jsonString)
    {
        try
        {
            Conversation conversation = JsonUtility.FromJson<Conversation>(jsonString);
            Debug.Log("New conversation");

            if(chatData != null)
            {
                chatData.UpdateConversation(conversation);
            }
            conversation = null;
        }
        catch
        {
            Debug.LogError("Failed to read conversation: " + jsonString);
        }
    }

    private void ProcessUserConversation(string jsonString)
    {
        try
        {
            UserConversation initData = JsonUtility.FromJson<UserConversation>(jsonString);
            Debug.Log("New user conversation");

            if(chatData != null)
            {
                chatData.UpdateUserConversation(initData);
            }
            initData = null;
        }
        catch
        {
            Debug.LogError("Failed to read user conversation: " + jsonString);
        }
    }

    public void Connect(string host, string port)
    {
        Debug.Log("Connecting::" + host + ":" + port);
        if (_useUWP)
        {
            ConnectUWP(host, port);
        }
        else
        {
            ConnectUnity(host, port);
        }
    }


#if UNITY_EDITOR
private void ConnectUWP(string host, string port)
#else
    private async void ConnectUWP(string host, string port)
#endif
    {
#if UNITY_EDITOR
    errorStatus = "UWP TCP client used in Unity!";
#else
        try
        {
            if (exchangeTask != null) StopExchange();

            socket = new Windows.Networking.Sockets.StreamSocket();
            Windows.Networking.HostName serverHost = new Windows.Networking.HostName(host);
            await socket.ConnectAsync(serverHost, port);

            Stream streamOut = socket.OutputStream.AsStreamForWrite();
            writer = new StreamWriter(streamOut) { AutoFlush = true };

            Stream streamIn = socket.InputStream.AsStreamForRead();
            reader = new StreamReader(streamIn);

            RestartExchange();
            successStatus = "Connected!";
        }
        catch (Exception e)
        {
            errorStatus = e.ToString();
        }
#endif
    }

    private void ConnectUnity(string host, string port)
    {
#if !UNITY_EDITOR
        errorStatus = "Unity TCP client used in UWP!";
#else
    try
    {
        if (exchangeThread != null) StopExchange();

        client = new System.Net.Sockets.TcpClient(host, Int32.Parse(port));
        stream = client.GetStream();
        reader = new StreamReader(stream);
        writer = new StreamWriter(stream) { AutoFlush = true };

        RestartExchange();
        successStatus = "Connected!";
    }
    catch (Exception e)
    {
        errorStatus = e.ToString();
    }
#endif
    }



    public void RestartExchange()
    {
#if UNITY_EDITOR
    if (exchangeThread != null) StopExchange();
    exchangeStopRequested = false;
    exchangeThread = new System.Threading.Thread(ExchangePackets);
    exchangeThread.Start();
#else
        if (exchangeTask != null) StopExchange();
        exchangeStopRequested = false;
        exchangeTask = Task.Run(() => ExchangePackets());
#endif
    }

    public void ExchangePackets()
    {
        while (!exchangeStopRequested)
        {
            if (writer == null || reader == null) continue;
            exchanging = true;

            if (lastTxPacket != null)
            {
                writer.WriteLine(lastTxPacket);
                Debug.Log("Sent data: " + lastTxPacket);
                lastTxPacket = null;
            }
            else
            {
                writer.WriteLine(Constants.CHAT_PACKET_CHECK_CONNECTION);
            }

            string received = null;

            received = reader.ReadLine();
//#if UNITY_EDITOR
//        byte[] bytes = new byte[client.SendBufferSize];
//        int recv = 0;
//        while (true)
//        {
//            recv = stream.Read(bytes, 0, client.SendBufferSize);
//            received += Encoding.UTF8.GetString(bytes, 0, recv);
//            if (received.EndsWith("\n")) break;
//        }
//#else
//            received = reader.ReadLine();
//#endif

            ProcessReceivedData(received);
            received = null;
                 
            exchanging = false;
        }
    }


    public void StopExchange()
    {
        exchangeStopRequested = true;

#if UNITY_EDITOR
    if (exchangeThread != null)
    {
        exchangeThread.Abort();
        stream.Close();
        client.Close();
        writer.Close();
        reader.Close();

        stream = null;
        exchangeThread = null;
    }
#else
        if (exchangeTask != null)
        {
            exchangeTask.Wait();
            socket.Dispose();
            writer.Dispose();
            reader.Dispose();

            socket = null;
            exchangeTask = null;
        }
#endif
        writer = null;
        reader = null;
    }

}


