# README
[AK_AQCS Software](https://github.com/GRAP-UdL-AT/ak_acquisition_system).



## Contents

| Folder                    | Description                                                                                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| remote_client_ak          | Code to manage Azure Kinect DK camera                                                                                                                                                                           |
| remote_client_generic     | This is a template for future development                                                                                                                                                                       |
| remote_client_zed         | Code to manage ZED 2 camera and Ardusimple GNSS receiver                                                                                                                                                        |
| remote_management_console | Desktop GUI based on Tkinter library. Offers the possibility of sending instructions to the remote devices.                                                                                                     |
| server_rest_api           | The server acts as an intermediary in the management of messages between remote clients and the managemen console, and stores information about of the instructions sent and received. It uses SQLite database. |
| .                         | .                                                                                                                                                                                                               |



## Basic requirements (TODO)
The requirements of software can be viewed in **requirements_linux.txt** and **requirements_win.txt**.
The software has been tested on Ubuntu Linux 20.04 and Windows 10.

## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html).
Please contact authors to report bugs juancarlos.miranda@udl.cat

## Citation
If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).





