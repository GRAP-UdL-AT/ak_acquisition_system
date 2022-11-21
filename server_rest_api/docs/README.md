# REST API testing

## REST API call reference with curl
If you want to test the server use curl as following:

### Authentication commands steps
```
curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/register/
curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/login/
curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/login/refresh/
```

### /logout/
```
curl -d "token=A_TOKEN_HERE" http://localhost:9000/authentication/logout/
```

### /commands/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=START_RECORD" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_RECORD" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=WAITING" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_REMOTE_CLIENT" http://localhost:9000/v1/commands/
```

### /config/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/config/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "sleep_time=5" http://localhost:9000/v1/config/
```

### /executed/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=RECORDING_ACK&start_record=''" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/command/1/
```

### /remote/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/remote/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'" http://localhost:9000/v1/remote/
```

## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html).
Please contact authors to report bugs juancarlos.miranda@udl.cat

## Citation
If you find this code useful, please consider citing:
[AK_ACQS - AK Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).
