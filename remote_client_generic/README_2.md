# README - Generic remote client
This is an example of a generic remote client. Use this code to test connections
between components in your acquisition system.
You can improve this as you want.
Use it as a dummy test process to test commands sent to the server from a central console.

* [TODO:COMPLETE THIS LINK ](https://github.com/juancarlosmiranda)

To start the server you must follow the steps below:
1. Install and run.
2. Start server console
3. Test connectivity.

## 1. Install and run
In Linux systems execute as follows:
```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./remote_client_generic-venv
source ./remote_client_generic-venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

For Windows systems follow these steps from command line CMD
```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv .\remote_client_generic-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
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
```
[DEFAULT]
protocol = http
host = 192.168.1.203
port = 9000
user = USER_ACCOUNT_HERE
password = USER_PASSWORD_HERE
sleep_time = 5
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

## Problems checklist
* Check LAN connection.
* Check user and password configurations.


## Package dependencies
This software need the following packages:
```
pip install certifi
pip install charset-normalizer
pip install idna
pip install requests
pip install urllib3
```
