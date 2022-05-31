# AK_ACQS - Generic remote client

This is an example of a generic remote client. Use this code to test connections between components in your acquisition
system. You can improve this as you want. Use it as a dummy test process to test commands sent to the server from a
central console.

![REMOTE_CLIENT_GENERIC](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_client_generic/docs/img/remote_client_generic_presentation.png?raw=true)

## Files and folder description

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
| remote_client_main.py | . | . |
| . | Apply changes in tables, reset database and load data from /src/initial_data_values/ | Linux |
| .sh | Executing main script | Linux |
| .bat | Executing main script | Win |
| README.md | This file | . |
| requirements_linux.txt | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |
| requirements_win.txt | Requirements <br>```pip install -r requirements_win.txt``` | Win |
| . | . | . |

To start the client you must follow the steps below:

1. Install and run.
2. Start server console
3. Test connectivity.
4. Problems checklist
5. Package distribution format

## 1. Install and run

In Linux systems execute as follows:

Create and activate environment.

```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./remote_client_generic-venv
source ./remote_client_generic-venv/bin/activate
pip install --upgrade pip
```

Install requirements.

```
pip install -r requirements_linux.txt
```

For Windows systems follow these steps from command line CMD

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_generic-venv\Scripts\activate.bat
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
data from the server.

```
[DEFAULT]
protocol = http
host = 192.168.43.110
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
sleep_time = 5
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

## 4. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## 5. Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------|
| Virtual environment          | N/A    | Testing in Ubuntu 20.04 and Windows 10 operating systems | . |

## Basic requirements (TODO)

The requirements of software can be viewed in **requirements_linux.txt** and **requirements_win.txt**. The software has
been tested on Ubuntu Linux 20.04 and Windows 10.

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).
