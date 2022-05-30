[AK_AQCS Software](https://github.com/GRAP-UdL-AT/ak_acquisition_system)

# AK_ACQS Azure Kinect Acquisition System

AK_ACQS is a software solution for data acquisition in fruit orchards using a sensor system boarded on a terrestrial
vehicle. It allows the coordination of computers and sensors through the sending of remote commands via a GUI. At the
same time, it adds an abstraction layer on library stack of each sensor, facilitating its integration. This software
solution is supported by a local area network (LAN), which connects computers and sensors from different manufacturers (
cameras of different technologies, GNSS receiver) for in-field fruit yield testing.

![AK_AQCS_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/ak_acqs_presentation.png?raw=true)

## Contents (TODO)

* Pre-requisites.
* Functionalities.
* Run.
* Files and folder description.
* Development tools and environment.

## Pre-requisites

### Hardware used

* MSI Modern 15 A10RBS-484XES (New Taipei, Zhonghe Dist) Computer 1
* Jetson Xavier NX (NVIDIA, Santa Clara, America) Computer 2.
* LAN (Local Area Network) to connect computers.
* [Azure Kinect DK camera](https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification) connected to the
  computer.
* GNSS
  receiver [Ardusimple SimpleRTK2B – Basic Starter Kit](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
  .
* [Stereolab ZED 2 camera](https://www.stereolabs.com/zed-2/) connected to the computer.

![SETUP_EXAMPLE](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/ak_acqs_example_of_use.png?raw=true)

### Software to manage devices 

* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [Canonical Ubuntu](https://ubuntu.com/#download) 20.04.
* [Jetson Pack](https://developer.nvidia.com/embedded/jetpack).
* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [Stereolabs SDK](https://www.stereolabs.com/developers/release/) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow
  this [steps](https://github.com/etiennedub/pyk4a/). You can find test basic examples with
  pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).

## Functionalities

The functionalities of AK_ACQS consist of remotely enabling and disabling clients, taking snapshots, starting and
stopping video recordings, as well as logging latitude and longitude coordinates during the video recording time.

* **[ENABLE REMOTE CLIENTS] allows the user to send an attention call to the devices to configure them in the initial
  state of listening to orders.
* **[TAKE CAPTURES] makes it easy for the user to capture short videos, automatically starting and stopping video or
  snapshot recording.
* **[START RECORDING/ STOP RECORDING] is the functionality that allows to send start and stop recording messages to all
  connected clients. Remote clients managing a GNSS receiver will start/stop operations for coordinate capture.
* **[DISABLE REMOTE CLIENTS], with this function the user remotely turns off the devices. These will stop operating when
  receiving and processing the message. The recorded files are stored on the host computers, just like the data
  collected by the GNSS receiver.

## Files and folder description

| Folder                    | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs)     | Documentation and explanations.     |
| [remote_client_generic/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic) | This is a template for future development, it is a dummy client can be used to test server connection.     |
| [remote_client_ak/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak) | Code to manage Azure Kinect DK camera                                                                      |
| [remote_client_zed/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed) | Code to manage ZED 2 camera and Ardusimple GNSS receiver                                                   |
| [remote_management_console/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console) | Desktop GUI based on Tkinter library. Offers the possibility of sending instructions to the remote devices.|
| [server_rest_api/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api) | The server acts as an intermediary in the management of messages between remote clients and the management <br> console, and stores information about of the instructions sent and received. It uses SQLite database. |
| .                         | . |

## Supplementary materials

| Folder                    | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| [REST API test/]https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/docs| Explanations about testing REST API.     |

## Run AK_SM_RECORDER

## Install

```
python ak_sm_recorder_main.py
```

### Windows (TODO)

Copy folder FOLDER_HERE and execute "FILENAME_EXE.EXE".

### Linux (TODO)

..

## Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------| 
| Windows      | .EXE    | .EXE | Executables are stored under build/ | 
| Linux        | .deb    | .deb | NOT IMPLEMENTED YET| 
| PIP          | .whl    | .whl | PIP packages are stored in build/ | 
| Virtual environment          | N/A    | N/A | . |
| . | . | . |

## Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| docs/ | Documentation |
| src/ | Source code |
| win_exe_conf/ | Specifications for building .exe files with Pyinstaller.|
| . | . |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| activate.bat | Activate environments in Windows | WIN |
| clean_files.bat | Clean files under CMD. | WIN |
| ak_sm_recorder_main.bat | Executing main script | WIN |
| build_pip.bat | Build PIP package to distribution | WIN |
| build_win.bat | Build .EXE for distribution | WIN |
| /src/ak_sm_recorder/__main__.py | Main function used in package compilation | Supported by Python |
| /ak_sm_recorder_main.py | Python main function | Supported by Python |
| setup.cfg | Package configuration PIP| Supported by Python |
| pyproject.toml | Package description pip| Supported by Python |
| . | . | . |

## Development tools and environment

* [curl](https://curl.se/)
* [Pyinstaller](https://pyinstaller.org).
* [Opencv](https://opencv.org/).
* [Curses for Python](https://docs.python.org/3/howto/curses.html) ```pip install windows-curses```.


## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[Juan Carlos Miranda](https://github.com/juancarlosmiranda).

## Acknowledgements

This work was funded by
the [Spanish Ministry of Science and Innovation and the Spanish Estate Research Agency](https://www.ciencia.gob.es) for
the grant RTI2018-094222-B-I00 ([PAgFRUIT project](http://www.pagfruit.udl.cat/en/)). Secretariat of Universities and
Research of the Department of Business and Knowledge of the [Generalitat de Catalunya](https://web.gencat.cat/) (grant
2017 SGR 646), and Fons Social Europeu ([FSE](https://ec.europa.eu/)) are also thanked for financing Juan Carlos
Miranda’s pre-doctoral fellowship ([2020 FI_B 00586](https://agaur.gencat.cat/)). The authors would also like to thank
the Institut de Recerca i Tecnologia Agroalimentàries ([IRTA](https://www.irta.cat)) for allowing the use of their
experimental fields, in particular Dr. Luís Asín and Dr. Jaume Lordán who have contributed to the success of this work.




<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main//docs/img/logo_udl.png" height="60px" alt="Universitat de Lleida"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main//docs/img/logo_goverment_calonia.png" height="60px" alt="Generalitat de Catalunya"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_min_science.png" height="60px" alt="Ministerio de Ciencia, Innovación y Universidades"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_UNIO_EUROPEA.png" height="60px" alt="Fons Social Europeu (FSE) "/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_AGAUR.png" height="60px" alt="AGAUR"/>




