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


## Acknowledgements

Acknowledgements
This work was partly funded by the Secretariat of Universities and Research of the Department of Business and Knowledge of the Generalitat de Catalunya (grant 2017 SGR 646) and the Spanish Ministry of Science, Innovation and Universities (PAgFRUIT project RTI2018-094222-B-I00). The first and aforementioned official institution and the Fons Social Europeu (FSE) are also thanked for financing Juan Carlos Miranda’s pre-doctoral fellowship (2020 FI_B 00586). The authors would also like to thank XXXXXX and XXXXXX for their support in XXXXXX.

<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/docs/img/logo_udl.png" height="60px" alt="Universitat de Lleida"/>&nbsp;&nbsp;&nbsp;
<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/docs/img/logo_goverment_calonia.png" height="60px" alt="Generalitat de Catalunya"/>&nbsp;&nbsp;&nbsp;
<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/docs/img/logo_min_science.png" height="60px" alt="Ministerio de Ciencia, Innovación y Universidades"/>&nbsp;&nbsp;&nbsp;
<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/docs/img/logo_UNIO_EUROPEA.png" height="60px" alt="Fons Social Europeu (FSE) "/>&nbsp;&nbsp;&nbsp;
<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/docs/img/logo_AGAUR.png" height="60px" alt="AGAUR"/>




