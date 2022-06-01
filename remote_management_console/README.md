# README - Remote Management Console 
Remote Management Console, this sends commands to the [REST API server](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/). It offers a basic interface to manage the acquisition system.

![REMOTE_MANAGEMENT_CONSOLE](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/remote_management_console/docs/img/management_console_presentation.png?raw=true)

## Files and folder description

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
| creating_env_console.sh | Automatically create Python environments | Linux |
| management_console_start.sh | Executing main script | Linux |
| main_management_console.py | Python main function | Supported by Python |
| activate.bat | Virtual environment | Win |
| requirements_linux.txt | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |
| requirements_win.txt | Requirements <br>```pip install -r requirements_win.txt``` | Win |

To start the remote console you must follow the steps below:
1. Install and run.
2. Start server console
3. Test connectivity.

## 1. Install and run

In Linux systems execute as follows:

Create and activate environment.
```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./remote_management_console-venv
source ./remote_management_console-venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

For Windows systems follow these steps from command line CMD.
```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_management_console-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
```


## 2. Start REST API server

For more information about "REST API server"
check [here](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/).
In server machine, start server executing from command line:

```
./server_rest_api/server_start.sh
```

## 3. Test connectivity

### 3.1 Changes in ./conf/ui_settings.conf
Check file for configurations settings in **./conf/ui_settings.conf**.
For example if your server is listening on IP 192.168.43.110, configure this number in field **host**.
Configure the username and password, put it in the respective fields as plain text. For a graphical example see [[1.1 Example configuration]](https://github.com/GRAP-UdL-AT/ak_acquisition_system#11-example-configuration---capturing-fruit-data-using-the-ak_acqs-software)
```
[DEFAULT]
protocol = http
host = 192.168.43.110
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
```


### 3.2 Check connection to server

After configure the allowed host, check connectivity to your server **HOST_SERVER_IP** with [curl](https://curl.se/) tool.
Where **USER_ACCOUNT_HERE** and **USER_PASSWORD_HERE** are the username and password you want.
```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
```

If the server is enabled, the response will be something like this:
```
$ curl -d "username=USER_ACCOUNT_HERE&password=USER_PASSWORD_HERE" http://HOST_SERVER_IP:9000/authentication/login/
{"access_token":"YIK0gxBdFdaAGZU4E0Y0bIOQx5FLap","expires_in":36000,"token_type":"Bearer","scope":"read write groups","refresh_token":"Tr6ugxQynW2hbpqnAsUdzVGVh9cO1F"}
```

## 5. Problems checklist

* Check LAN connection.
* Check user and password configurations.

## 6. Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------|
| Virtual environment          | N/A    | Testing in Ubuntu 20.04 and Windows 10 operating systems | . |


## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).
