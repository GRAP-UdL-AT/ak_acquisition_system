# AK_ACQS Azure Kinect Acquisition System

AK_ACQS is a software solution for data acquisition in fruit orchards using a sensor system boarded on a terrestrial
vehicle. It allows the coordination of computers and sensors through the sending of remote commands via a GUI. At the
same time, it adds an abstraction layer on library stack of each sensor, facilitating its integration. This software
solution is supported by a local area network (LAN), which connects computers and sensors from different manufacturers (
cameras of different technologies, GNSS receiver) for in-field fruit yield testing.

![AK_AQCS_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/ak_acqs_presentation.png?raw=true)

## Contents

1. Pre-requisites.
2. Functionalities developed.
3. Files and folder description.
4. Development tools and environment.

## 1. Pre-requisites

This section explains aspects related to the pre-requisites needed to run AK_ACQS, hardware and software used in the
experiments.

### 1.1 Example configuration - Capturing fruit data using the AK_ACQS software

The following figure shows an example configuration, which will be used in other sections as a starting point for the
explanations.

![SETUP_EXAMPLE](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/ak_acqs_example_of_use.png?raw=true)

### 1.2 Hardware

* MSI Modern 15 A10RBS-484XES (New Taipei, Zhonghe Dist) Computer 1.
* Jetson Xavier NX (NVIDIA, Santa Clara, America) Computer 2.
* LAN (Local Area Network) to connect computers.
* [Azure Kinect DK camera](https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification) connected to the
  computer.
* GNSS
  receiver [Ardusimple SimpleRTK2B – Basic Starter Kit](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
  .
* [Stereolab ZED 2 camera](https://www.stereolabs.com/zed-2/) connected to the computer.

### 1.3 Software

* [Canonical Ubuntu](https://ubuntu.com/#download) 20.04.
* [Jetson Pack](https://developer.nvidia.com/embedded/jetpack).
* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [Stereolabs SDK](https://www.stereolabs.com/developers/release/) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow
  this [steps](https://github.com/etiennedub/pyk4a/). You can find test basic examples with
  pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).

## 2. Functionalities developed

The functionalities of AK_ACQS consist of remotely enabling and disabling clients, taking snapshots, starting and
stopping video recordings, as well as logging latitude and longitude coordinates during the video recording time.

* **[ENABLE REMOTE CLIENTS]** allows the user to send an attention call to the devices to configure them in the initial
  state of listening to orders.
* **[TAKE CAPTURES]** makes it easy for the user to capture short videos, automatically starting and stopping video or
  snapshot recording.
* **[START RECORDING/ STOP RECORDING]** is the functionality that allows to send start and stop recording messages to
  all connected clients. Remote clients managing a GNSS receiver will start/stop operations for coordinate capture.
* **[DISABLE REMOTE CLIENTS]**, with this function the user remotely turns off the devices. These will stop operating
  when receiving and processing the message. The recorded files are stored on the host computers, just like the data
  collected by the GNSS receiver.

## 3. Files and folder description

| Folder                    | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| [docs/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs)     | Documentation and explanations.     |
| [remote_client_generic/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic) | This is a template for future development, it is a dummy client can be used to test server connection.     |
| [remote_client_ak/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak) | Code to manage Azure Kinect DK camera                                                                      |
| [remote_client_zed/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed) | Code to manage ZED 2 camera and Ardusimple GNSS receiver                                                   |
| [remote_management_console/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console) | Desktop GUI based on Tkinter library. Offers the possibility of sending instructions to the remote devices.|
| [server_rest_api/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api) | The server acts as an intermediary in the management of messages between remote clients and the management <br> console, and stores information about of the instructions sent and received. It uses SQLite database. |

## 4. Development tools

### 4.1 Download this repository

From Linux systems, run this script at the command line to automatically create directory hierarchies for the project's
development environments. Then use the "create_env_xxxxxx.sh" scripts for each component to load the Python
dependencies.

```
SOME_INLINE_SCRIPT_HERE
```

```
SCRIPT INLINE will make this
git clone https://github.com/GRAP-UdL-AT/ak_acquisition_system.git
```

### 4.2 Supplementary materials

Documents and explanations accompanying AK_ACQS.

| Folder                    | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| [REST API test/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api/docs/)| Explanations about testing REST API.     |
| [Notes for developers/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/NOTES_FOR_DEVELOPERS.md)| Explanations about development environment     |

### 4.3 Package distribution format

Distribution of AK_ACQS components.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------| 
| Virtual environment          | N/A    | N/A | All components of this software run in separate virtual environments. |

### 4.3 Supported operating systems

The following table shows each component of AK_ACQS and the operating systems on which they have been tested.

| Component                    | Linux | Windows | Jetpack|
|---------------------------|---|---|---|
| [remote_client_generic/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_generic) | YES |  YES | YES |
| [remote_client_ak/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_ak) | YES |  YES | N/T |
| [remote_client_zed/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_client_zed) | YES |  N/T | YES |
| [remote_management_console/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/remote_management_console) | YES |  YES | N/T |
| [server_rest_api/](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/server_rest_api) | YES |  N/T | YES |

**References:**

* N/T --> The software has not yet been tested under the operating system at the time of publication.
* YES --> Tested in operating system.
* NO --> Support for this operating system is not yet available.

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:

```
@article{SURNAME_YEAR,
    Author = {Miranda, Juan Carlos and Gen{\'e}-Mola, Jordi and Arn{\'o}, Jaume and Gregorio, Eduard},
    Title = {AKFruitData: a dual software application for Azure Kinect cameras to acquire and extract informative data in yield tests performed in fruit orchard environments},
    Journal = {Submitted},
    Year = {YEAR}
}
```

## Acknowledgements

This work was funded by the Spanish Ministry of Science and Innovation and the Spanish Estate Research Agency through
grant RTI2018-094222-B-I00 (PAgFRUIT project). This work was also supported by the Secretaria d’Universitats i Recerca
del Departament d’Empresa i Coneixement de la Generalitat de Catalunya under Grant 2017-SGR-646. The Secretariat of
Universities and Research of the Department of Business and Knowledge of the Generalitat de Catalunya and Fons Social
Europeu (FSE) are also thanked for financing Juan Carlos Miranda’s pre-doctoral fellowship (2020 FI_B 00586). The work
of Jordi Gené-Mola was supported by the Spanish Ministry of Universities through a Margarita Salas postdoctoral grant
funded by the European Union - NextGenerationEU. The authors would also like to thank the Institut de Recerca i
Tecnologia Agroalimentàries (IRTA) for allowing the use of their experimental fields, and in particular Dr. Luís Asín
and Dr. Jaume Lordán who have contributed to the success of this work.


<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main//docs/img/logo_udl.png" height="60px" alt="Universitat de Lleida"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main//docs/img/logo_goverment_calonia.png" height="60px" alt="Generalitat de Catalunya"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_min_science.png" height="60px" alt="Ministerio de Ciencia, Innovación y Universidades"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_UNIO_EUROPEA.png" height="60px" alt="Fons Social Europeu (FSE) "/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_acquisition_system/blob/main/docs/img/logo_AGAUR.png" height="60px" alt="AGAUR"/>




