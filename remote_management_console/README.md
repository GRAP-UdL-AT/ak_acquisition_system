# README - Remote Management Console 
Remote Management Console, this sends commands to the [REST API server](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/). It offers a basic interface to manage the acquisition system.

![REMOTE_MANAGEMENT_CONSOLE](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_management_console/docs/img/management_console_presentation.png?raw=true)

## Contents

1. Files and folder description.
2. Package distribution format.
3. Steps to start the client for the first time.


## 1. Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console/docs/) | Documentation |
| [log/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console/log/) | Execution log files |
| [src/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console/src/) | Source code |
| [src/conf/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console/src/conf/) | Client configuration files |


Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| creating_env_console.sh | Automatically creates Python environments | Linux |
| management_console_start.sh | Executing main script | Linux |
| main_management_console.py | Python main function | Supported by Python |
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

* [Linux] Create and activate the Python environment as follows:

```
./create_env_console.sh
```

For more information on the folder hierarchy used in development environments, go
to [[Notes for developers]](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/NOTES_FOR_DEVELOPERS.md)

* [Windows] Follow these steps from command line CMD.

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_management_console-venv\Scripts\activate.bat
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

### 3.5. Run

Run remote console in Linux systems.

```
./management_console_start.sh
```

## 4. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## 5. Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------|
| Virtual environment          | N/A    | Testing in Ubuntu 20.04 and Windows 10 operating systems | . |


## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[AK_ACQS - ak Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).
