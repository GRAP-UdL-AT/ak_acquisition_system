#README Remote client for multi-camera recording
The solution allows recording data from cameras housed in different computers, focusing on the same scene. The cameras are of different brands, models and technologies. Images are recorded with GPS coordinates.
It is a solution made up of three components: API server, remote clients connected to cameras, and user interface.
The functions are as follows:
API server: receive requests, send group messages.
Remote client: receives instructions from a central server, hosts devices (cameras, GPS). Make recordings and store data from them.
User interface: allows managing the operation of the assembly and issuing remote commands.

To start the client you must follow the steps below:
1. Install and run.
2. Start server console
3. Test connectivity.
4. Check Azure Kinect settings
5. Check recorded videos



## 3. Test connectivity
### 3.1 Changes in ./conf/client_settings.conf
Check file for configurations settings in **conf/client_settings.conf**.
For example if your server is listening on IP 192.168.43.110, configure this number in field **host**.
Configure the username and password, put it in the respective fields as plain text.
Set the sleep time, this parameter ensures that the remote client will remain waiting to query data from the server.
Set **path_video_output** to configure the path to store videos in .mkv format.

```
[DEFAULT]
protocol = http
host = 192.168.43.110
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
sleep_time = 1
path_video_output = C:\remote_client_ka\recorded_video
```

### 3.2 Check connection to server 
After configure the allowed host, check connectivity to your server with [curl](https://curl.se/) tool.
Where **USER_ACCOUNT_HERE** and **USER_PASSWORD_HERE** are the username and password you want.
```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://localhost:9000/authentication/login/
```

If the server is enabled, the response will be something like this:
```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://localhost:9000/authentication/login/
{"access_token":"YIK0gxBdFdaAGZU4E0Y0bIOQx5FLap","expires_in":36000,"token_type":"Bearer","scope":"read write groups","refresh_token":"Tr6ugxQynW2hbpqnAsUdzVGVh9cO1F"}
```

## 4. Check Azure Kinect settings ./conf/kinect_azure_settings.conf
You must be sure that Azure Kinect camera is connected and recognized by the operating system.
**PUT_HERE_LINK TO AZURE KINECT CONFIG **
In the file **./conf/kinect_azure_settings.conf** there are stored settings related to the camera.
Settings parameters are explained in **[OFICIAL_SITE]** 
```
[DEFAULT]
color_resolution=RES_1080P
color_format=COLOR_MJPG
depth_mode=NFOV_UNBINNED
camera_fps=FPS_30,
synchronized_images_only=True
depth_delay_off_color_usec=0
wired_sync_mode=STANDALONE
subordinate_delay_off_master_usec=0
disable_streaming_indicator=True
```


## Problems checklist
* Check LAN connection.
* Check user and password configurations.

## Package dependencies (TODO)
This software need the following packages:
```
py4ka
...

```

