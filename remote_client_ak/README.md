# AK_ACQS - Remote client Azure

This document describes the steps required to run the remote client that records data from the Azure Kinect camera as
part of the ["AK_ACQS"](https://github.com/GRAP-UdL-AT/ak_acquisition_system) core solution. The core solution is made
up of three components:

* [REST API server:](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/) receive requests,
  send group messages.
* Remote clients: receives instructions from a central server, hosts devices. Make recordings and store data from them.
* [Remote management console](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console):
  allows managing the operation of the assembly and issuing remote commands.

![REMOTE_CLIENT_AK](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_client_ak/docs/img/remote_client_azure_presentation.png?raw=true)

## Contents

1. Files and folder description.
2. Package distribution format.
3. Steps to start the client for the first time.

## 1. Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| [conf/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak/conf/) | Client configuration files |
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak/docs/) | Documentation |
| [log/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak/log/) | Execution log files |
| [src/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak/src/) | Source code |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| creating_env_ak.sh | Automatically creates Python environments | Linux |
| remote_client_ak_start.sh | Executing main script | Linux |
| main_client_azure.py | Python main function | Supported by Python |
| activate.bat | Virtual environment | Win |
| requirements_linux.txt | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |
| requirements_win.txt | Requirements <br>```pip install -r requirements_win.txt``` | Win |

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
* 3.4. Check Azure Kinect camera settings.
* 3.5. Run.
* 3.6. Check recorded videos.
* 3.7. Problems checklist.

### 3.1. Install

* Install Azure Kinect camera drivers by following the instructions
  at [azure_kinect_notes](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs/azure_kinect_notes), depending on whether your operating
  system is Linux or Windows.

* [Linux] Create and activate the Python environment as follows:

```
./create_env_ak.sh
```

For more information on the folder hierarchy used in development environments, go
to [[Notes for developers]](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs/NOTES_FOR_DEVELOPERS.md)

* [Windows] Follow these steps from command line CMD.

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_ak-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
```

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

Check file for settings in **conf/client_settings.conf**. For example if your server is listening on IP 192.168.43.110,
configure this number in field **host** and put the username and password, as plain text. Set the **sleep_time**, this
parameter ensures that the remote client will remain waiting to query data from the server. Set **path_video_output** to
configure the path to store videos in .mkv format. For a graphical example
see [[1.1 Example configuration]](https://github.com/GRAP-UdL-AT/ak_acquisition_system#11-example-configuration---capturing-fruit-data-using-the-ak_acqs-software)

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

### 3.4 Check Azure Kinect camera settings ./conf/kinect_azure_settings.conf

You need to make sure that the Azure Kinect camera is connected and recognized by the operating system. Follow the
instructions in this ["azure_kinect_notes"](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs/azure_kinect_notes) section if you
haven't installed the camera before. In the file **./conf/kinect_azure_settings.conf** there are camera-related settings
stored. Settings parameters are explained
in [**[Azure Kinect Sensor SDK]**](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/index.html)

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

### 3.5. Run

Run remote client in Linux systems.

```
./remote_client_ak_start.sh
```

### 3.6. Check recorded videos (TODO)

..

### 3.7. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[AK_ACQS - ak Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).
