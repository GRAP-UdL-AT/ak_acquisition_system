# AK_ACQS - REST API server

REST API server that centralizes the sending and receiving of remote commands. It is responsible for coordinating
actions between remote clients and a graphical user console. Where each remote client can have different devices
connected. In this work remote clients have been used to control Azure Kinect, ZED camera, ArduSimple GNSS devices. To
make it as simple as possible, the data was stored in the db.sqlite3 file.

![REST_API_SERVER_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/server_rest_api/docs/img/rest_api_server_presentation.png?raw=true)

## Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| [api_rest/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/api_rest) | Settings for Django REST Framework |
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/docs) | Documentation |
| [scripts/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/scripts/) | Useful tools |
| [src/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/src/) | Source code |
| . | . |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| broadcast.db.sqlite3 | Message database | . |
| creating_env_server.sh | Automatically create Python environments | Linux |
| delete_reset_database.sh | Apply changes in tables, reset database and load data from /src/initial_data_values/ | Linux |
| rest_api_server_start.sh | Executing main script | Linux |
| requirements_linux | Requirements <br>```pip install -r requirements_linux.txt``` | Linux |


To start the server you must follow the steps below:

1. Install and run.
2. Create database settings.
3. Start server
4. Test connectivity.

## 1. Install and run

In Linux systems execute as follows:

Create and activate environment.
```
python3 -m pip install python-venv
pip3 install python-venv
python3 -m venv ./server_rest_api-venv
source ./server_rest_api-venv/bin/activate
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

## 2. Create database settings

### 2.1 Change parameters in **/src/api_rest/settings.py** file.

Generate a new key with command line

```
$ echo "a_password_to_set" | sha256sum
```

copy generated string into field **SECRET_KEY** between single quotes.

```
SECRET_KEY = '0d235b95999cdad00e4da9a48b9e85f7cec377712232785df16b44b094c340c0'
```

Configure users and passwords and upload them into the file **/scr/initial_data_values/user_data.json/**. Follow the
instructions in the script.

```
python ./manage.py runscript manage_password_str --chdir ./scripts/
```

If you want change the secret keys values in **/src/api_rest/settings.py**, you must change the content in **
/src/initial_data_values/oauth2_provider.json** too. Configure fields in client_id and client_secret

```
# **/src/api_rest/settings.py**
CLIENT_ID = 'SUPER_SECRET_CLIENT_ID_HERE'
CLIENT_SECRET = 'SUPER_SECRET_CLIENT_KEY_HERE'
```

Configure changes in /src/initial_data_values/oauth2_provider.json

```
[
    {
        "model": "oauth2_provider.application",
        "pk": 1,
        "fields": {
            "client_id": "SUPER_SECRET_CLIENT_ID_HERE",
            "user": null,
            "redirect_uris": "",
            "client_type": "confidential",
            "authorization_grant_type": "password",
            "client_secret": "SUPER_SECRET_CLIENT_KEY_HERE",
            "name": "",
            "skip_authorization": false,
            "created": "2021-08-01T15:00:00.000Z",
            "updated": "2021-08-01T15:00:00.000Z"}
    }
]
```

The content of **CLIENT_ID** and **CLIENT_SECRET** must be the same in both files ****

Configure **/src/api_rest/settings.py** file. For example, if your REST API server is IP 192.168.43.110 in your LAN, you
have to write in **settings.py** file as follows:

```
# /src/api_rest/settings.py 
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '192.168.43.110', 'localhost']
```

### 2.2 Load database with initial values

Loads initial data into database. reset initial configurations with

```
./delete_reset_database.sh
```

## 3. Start server

For star the server process in Linux systems, execute as follows:

```
./rest_api_server_start.sh
```

## 4. Test connectivity

After configure the allowed host, check connectivity to your server with [curl](https://curl.se/) tool. Where **user1**
and **strong_pass1** are the username and password you want.

```
$ curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/login/
```

If the server is enabled, the response will be something like this:

```
$ curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/login/
{"access_token":"YIK0gxBdFdaAGZU4E0Y0bIOQx5FLap","expires_in":36000,"token_type":"Bearer","scope":"read write groups","refresh_token":"Tr6ugxQynW2hbpqnAsUdzVGVh9cO1F"}
```

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
