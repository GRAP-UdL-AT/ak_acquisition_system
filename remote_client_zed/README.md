# AK_ACQS - Remote client ZED

The solution allows recording data from cameras housed in different computers, focusing on the same scene. The cameras
are of different brands, models and technologies. Images are recorded with GPS coordinates. It is a solution made up of
three components: [REST API server](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/), remote clients connected to cameras, and user interface. The functions are as follows:
REST API server: receive requests, send group messages. Remote client: receives instructions from a central server, hosts
devices (cameras, GNSS). Make recordings and store data from them. User interface: allows managing the operation of the
assembly and issuing remote commands.

![REMOTE_CLIENT_ZED](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_client_zed/docs/img/remote_client_zed_presentation.png?raw=true)

## Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| [conf/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed/conf/) | Client configuration files |
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed/docs/) | Documentation |
| [log/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed/log/) | Execution log files |
| [src/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed/src/) | Source code |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| clean_files.sh | Clean recoded videos. | Linux |
| enable_port.sh | Script that enable port for GNSS. | Linux |
| creating_env_zed.sh | Automatically creates Python environments | Linux |
| remote_client_zed_start.sh | Executing main script  from shell for ZED 2 | Linux |
| remote_client_zed_gnss_start.sh | Executing main script  from shell for ZED 2 + GNSS | Linux |
| main_client_zed.py | Executing main script ZED 2 | Supported by Python |
| main_client_zed_gnss.py | Executing main script ZED 2 + GNSS receiver | Supported by Python |
| requirements_jetson_xavier.txt | Requirements <br>```requirements_jetson_xavier.txt``` | Jetpack |
| requirements_linux.txt | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |


To start the client you must follow the steps below:

1. Install and run.
2. Start server console.
3. Test connectivity.
4. Check Azure Kinect settings.
5. Check recorded videos.
6. Problems checklist.
7. Package distribution format.

## 1. Install and run

In Linux systems execute as follows:

Create and activate environment.

```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./remote_client_zed-venv
source ./remote_client_ka-venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

For Windows systems follow these steps from command line CMD.

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_zed-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
```

## 2. Start REST API server

For more information about "REST API server"
check [here](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/)
In server machine, start server executing from command line:

```
./server_rest_api/server_start.sh
```

## 3. Test connectivity

### 3.1 Changes in ./conf/client_settings.conf

Check file for configurations settings in **conf/client_settings.conf**. For example if your server is listening on IP
192.168.43.110, configure this number in field **host**. Configure the username and password, put it in the respective
fields as plain text. Set the sleep time, this parameter ensures that the remote client will remain waiting to query
data from the server. Set **path_video_output** to configure the path to store videos in .mkv format.

```
[DEFAULT]
protocol = http
host = 192.168.43.110
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
sleep_time = 1
path_video_output = /home/user/development/recorded_zed_video
```

### 3.2 Check connection to server

After configure the allowed host, check connectivity to your server **HOST_SERVER_IP** with [curl](https://curl.se/) tool. Where **
USER_ACCOUNT_HERE** and **USER_PASSWORD_HERE** are the username and password you want.

```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
```

If the server is enabled, the response will be something like this:

```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
{"access_token":"YIK0gxBdFdaAGZU4E0Y0bIOQx5FLap","expires_in":36000,"token_type":"Bearer","scope":"read write groups","refresh_token":"Tr6ugxQynW2hbpqnAsUdzVGVh9cO1F"}
```

## 4. Check Azure Kinect settings ./conf/zed_settings.conf

You must be sure that ZED 2 camera is connected and recognized by the operating system.
[ZED 2](https://www.stereolabs.com/zed-2/).
In the file **./conf/zed_settings.conf** there are stored settings related to the camera. Settings parameters are
explained in [API Documentation](https://www.stereolabs.com/docs/api/).
For a graphical example with all the components of AK_ACQS see [[1.1 Example configuration]](https://github.com/GRAP-UdL-AT/ak_acquisition_system#11-example-configuration---capturing-fruit-data-using-the-ak_acqs-software)


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

The data recorded is saved in folders "recorded_gnss/" and "recorded_video/".

## 6. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## 7. Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------|
| Virtual environment          | N/A    | Testing in Ubuntu 20.04 and Windows 10 operating systems | . |

## Basic requirements (TODO)

The requirements of software can be viewed in **requirements_linux.txt** and **requirements_jetson_xavier.txt**. The
software has been tested on Ubuntu Linux 20.04 and Jetpack.

### Package dependencies (TODO)

This software need the following packages:

```
pip install pyzed
pip install path
pip install opencv-python
...
```

### Special notes about Jetson Xavier platform

Install ZED 2 camera following instructions in [SDK Downloads](https://www.stereolabs.com/developers/release/)

```
python -m pip install --ignore-installed /usr/local/zed/pyzed-3.5-cp36-cp36m-linux_aarch64.whl
```

Replace "/usr/local/zed/pyzed-3.5-cp36-cp36m-linux_aarch64.whl" with last version of ZED 2 API.

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).
