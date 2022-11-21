#!/bin/bash
# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
# Based on steps from https://www.stereolabs.com/docs/app-development/python/install/


wget https://download.stereolabs.com/zedsdk/3.7/cu115/ubuntu20
chmod 755 ubuntu20
./ubuntu20

python3 -m pip install cython numpy opencv-python pyopengl

cd "/usr/local/zed/"
python3 get_python_api.py

# Tools
/usr/local/zed/tools/ZED_Explorer
/usr/local/zed/tools/ZED_Depth_Viewer
