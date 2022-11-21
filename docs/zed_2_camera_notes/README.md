![SOFTWARE_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_acquisition_system/tree/main/docs/zed_2_camera_notes/zed_2_presentation.png?raw=true)

# README - Stereolabs ZED 2 camera

This document contains instructions/notes on how to install the Stereolabs ZED 2 camera. Here we collect experiences
that have arisen with the development
of [AK_ACQS - ak_acquisition_system](https://github.com/GRAP-UdL-AT/ak_acquisition_system/). If you find this useful let
me know.

This is not intended to replace official documents, it is produced as a complementary guide in my learning. Official
Stereolabs documents can be found at:

* [Stereolab ZED 2 camera](https://www.stereolabs.com/zed-2/)
* [Stereolabs SDK](https://www.stereolabs.com/developers/release/)
* [Install the ZED Python API](https://www.stereolabs.com/docs/app-development/python/install/)
* [Tutorials](https://www.stereolabs.com/docs/tutorials/)

Official tools to manage the camera and sensors can be found in:

* [ZED EXPLORER](https://www.stereolabs.com/zed-2/)
* [ZED Depth](https://www.stereolabs.com/zed-2/)

This document is organized as following:

*
    1. Fast setup using scripts in Linux systems.
*
    2. Installing in Linux environments.
*
    3. Installing in Windows 10 environments.

## 1. Fast setup using scripts in Linux systems

In Linux systems you can install packages using Bash scripts, tested in Ubuntu 20.04. A super fast script for impatient
people, copy and paste it!!!

```
git clone https://github.com/juancarlosmiranda/zed_2_camera_notes.git && cd zed_2_camera_notes && chmod 755 install_zed_2_camera_linux.sh
```

Check the camera with this tool **[ZED Explorer]**.

```
/usr/local/zed/tools/ZED_Explorer
```

Use **[ZED Depth Viewer]**.

```
/usr/local/zed/tools/ZED_Depth_Viewer
```

## 2. Installing in Linux environments (PENDING).

## 3. Installing in Windows 10 environments (PENDING).

This section will be updated in the next iterations.

* (Windows installation instructions)

## Authorship

Please contact author to report bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[AK_ACQS - AK Acquisition System](https://github.com/GRAP-UdL-AT/ak_acquisition_system).