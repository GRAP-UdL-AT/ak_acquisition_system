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

## 1. Install and run
In Linux systems execute as follows:
```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./remote_client_zed-venv
source ./remote_client_zed-venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

## 2. Start server console
In server machine, start server executing from command line: 
```
./server_rest_api/server_start.sh
```

## 3. Test connectivity
### 3.1 Changes in ./conf/client_settings.conf
Check file for configurations settings in **conf/client_settings.conf**.
For example if your server is listening on IP 192.168.1.203, configure this number in field **host**.
Configure the username and password, put it in the respective fields as plain text.
Set the sleep time, this parameter ensures that the remote client will remain waiting to query data from the server.
Set **path_video_output** to configure the path to store videos in .svo format.

```
[DEFAULT]
protocol = http
host = 192.168.1.203
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
sleep_time = 1
path_video_output = C:\remote_client_zed\recorded_video
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

## 4. Check Azure Kinect settings ./conf/zed_settings.conf
You must be sure that ZED 2 camera is connected and recognized by the operating system.
**PUT_HERE_LINK TO ZED 2 CONFIG **
In the file **./conf/zed_settings.conf** there are stored settings related to the camera.
Settings parameters are explained in **[OFICIAL_SITE]** 
```
[DEFAULT]
camera_disable_self_calib = False
camera_fps = 0
camera_image_flip = FLIP_MODE.AUTO
camera_resolution = RESOLUTION.HD1080
coordinate_system = COORDINATE_SYSTEM.IMAGE
coordinate_units = UNIT.MILLIMETER
depth_maximum_distance = -1.0
depth_minimum_distance = -1.0
depth_mode = DEPTH_MODE.PERFORMANCE
depth_stabilization = True
enable_image_enhancement = True
enable_right_side_measure = False
input = ''
optional_opencv_calibration_file = ''
#optional_settings_path = ''
sdk_gpu_id = -1
sdk_verbose = False
#sdk_verbose_log_file = ''
sensors_required = False
svo_real_time_mode = False
```

## 5. Check recorded videos (TODO)
..

## Problems checklist
* Check LAN connection.
* Check user and password configurations.

## Package dependencies (TODO)
This software need the following packages:
```
pip install pyzed
pip install path
pip install opencv-python
...

```
## Special notes about Jetson Xavier platform
Install ZED 2 camera following instructions in [SDK Downloads](https://www.stereolabs.com/developers/release/)
```
python -m pip install --ignore-installed /usr/local/zed/pyzed-3.5-cp36-cp36m-linux_aarch64.whl
```


## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html).
Please contact authors to report bugs juancarlos.miranda@udl.cat

## Citation
If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).
