# AK_ACQS - Generic remote client

This is an example of a generic remote client. Use this code to test connections between components in your acquisition
system. You can improve this as you want. Use it as a dummy test process to test commands sent to the server from a
central console.

![REMOTE_CLIENT_GENERIC](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_client_generic/docs/img/remote_client_generic_presentation.png?raw=true)

## Contents

1. Files and folder description.
2. Package distribution format.
3. Steps to start the client for the first time.


## 1. Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| [conf/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic/conf/) | Client configuration files |
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic/docs/) | Documentation |
| [log/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic/log/) | Execution log files |
| [src/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic/src/) | Source code |
| . | . |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| creating_env_generic.sh | Automatically creates Python environments     | Linux |
| remote_client_generic_start.sh | Executing main script | Linux |
| remote_client_main.py | Python main function | Supported by Python |
| .bat | Executing main script | Win |
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
* 3.4. Run.
* 3.6. Problems checklist.

### 3.1. Install

* [Linux] Create and activate the Python environment as follows:

```
./create_env_generic.sh
```

For more information on the folder hierarchy used in development environments, go
to [[Notes for developers]](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/NOTES_FOR_DEVELOPERS.md)

* [Windows] Follow these steps from command line CMD.

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_generic-venv\Scripts\activate.bat
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
sleep_time = 5
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

### 3.6. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[AK_ACQS - ak Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).
