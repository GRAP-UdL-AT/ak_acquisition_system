# AK_ACQS - Remote client ZED

This document describes the steps required to run the remote client that records data from the ZED 2 camera and
Ardusimple SimpleRTK2B as part of the ["AK_ACQS"](https://github.com/GRAP-UdL-AT/ak_acquisition_system) core solution.
The core solution is made up of three components:

* [REST API server:](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/) receive requests,
  send group messages.
* Remote clients: receives instructions from a central server, hosts devices. Make recordings and store data from them.
* [Remote management console](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console):
  allows managing the operation of the assembly and issuing remote commands.

![REMOTE_CLIENT_ZED](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_client_zed/docs/img/remote_client_zed_presentation.png?raw=true)

## Contents

1. Files and folder description.
2. Package distribution format.
3. Steps to start the client for the first time.

## 1. Files and folder description

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
| main_client_zed_gnss.py | Executing main script ZED 2 + Ardusimple SimpleRTK2B | Supported by Python |
| requirements_jetson_xavier.txt | Requirements <br>```requirements_jetson_xavier.txt``` | Jetpack |
| requirements_linux.txt | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |

## 2. Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------|
| Virtual environment          | N/A    | Testing in Ubuntu 20.04 and Windows 10 operating systems | . |

## 3. Steps to start the client for the first time

To start the client, you need to follow the steps below:

* 3.1. Install.
* 3.2. Start REST API server.
* 3.3. Test connectivity.
* 3.4. Check ZED 2 camera settings.
* 3.5. Run.
* 3.6. Check recorded videos.
* 3.7. Problems checklist.

### 3.1. Install

* Install ZED 2 camera drivers by following the instructions
  at [zed_2_camera_notes](https://github.com/juancarlosmiranda/zed_2_camera_notes), depending on whether your operating
  system is Linux or Windows.

* [Linux] Create and activate the Python environment as follows:

```
./create_env_zed.sh
```

* [Jetpack] In Jetson platforms:

```
./create_env_zed_jetson.sh
```

* [Windows 10] Follow these steps from command line CMD.

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_zed-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_windows.txt
```

Some requirements are different between platforms, versions can be viewed in **requirements_linux.txt** , **
requirements_jetson_xavier.txt**, **requirements_windows.txt** for Ubuntu Linux 20.04 ,Jetpack and Windows 10
respectively.

For more information on the folder hierarchy used in development environments, go
to [[Notes for developers]](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/NOTES_FOR_DEVELOPERS.md)

### 3.2. Start REST API server

This step assumes that
the ["REST API server"](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/) is configured
and running. For more information about this component
check [here](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/). On the server machine,
start server by running the following command line:

```
./server_rest_api/server_start.sh
```

### 3.3. Test connectivity

#### 3.3.1 Changes in ./conf/client_settings.conf

Check file for configurations settings in **conf/client_settings.conf**. For example if your server is listening on IP
192.168.43.110, configure this number in field **host**. Configure the username and password, put it in the respective
fields as plain text. Set the sleep time, this parameter ensures that the remote client will remain waiting to query
data from the server. Set **path_video_output** to configure the path to store videos in .mkv format.

Check file for settings in **conf/client_settings.conf**. For example if your server is listening on IP 192.168.43.110,
configure this number in field **host** and put the username and password, as plain text. Set the **sleep_time**, this
parameter ensures that the remote client will remain waiting to query data from the server. Set **path_video_output** to
configure the path to store videos in [SVO format](https://www.stereolabs.com/docs/video/recording/). For a graphical
example
see [[1.1 Example configuration]](https://github.com/GRAP-UdL-AT/ak_acquisition_system#11-example-configuration---capturing-fruit-data-using-the-ak_acqs-software)

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

#### 3.3.2 Check connection to server (optional)

After configure the allowed host, check connectivity to your server **HOST_SERVER_IP** with [curl](https://curl.se/)
tool. Where **
USER_ACCOUNT_HERE** and **USER_PASSWORD_HERE** are the username and password you want.

```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
```

If the server is enabled, the response will be something like this:

```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
{"access_token":"YIK0gxBdFdaAGZU4E0Y0bIOQx5FLap","expires_in":36000,"token_type":"Bearer","scope":"read write groups","refresh_token":"Tr6ugxQynW2hbpqnAsUdzVGVh9cO1F"}
```

### 3.4 Check ZED 2 camera settings ./conf/zed_settings.conf

You need to make sure that the ZED 2 camera is connected and recognized by the operating system. Follow the instructions
in this [zed_2_camera_notes](https://github.com/juancarlosmiranda/zed_2_camera_notes) section if you haven't installed
the camera before. In the file **./conf/zed_settings.conf** there are camera-related settings stored. Settings
parameters are explained in [**[API Documentation]**](https://www.stereolabs.com/docs/api/).

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

### 3.5. Run

Run remote client in Linux systems.

```
./remote_client_ak_start.sh
```

### 3.6. Check recorded videos (TODO)

The data recorded is saved in folders "recorded_gnss/" and "recorded_video/".

## 3.7. Problems checklist

* Check LAN connection.
* Check user and password configurations.

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
[AK_ACQS - ak Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).

