#!/bin/bash
# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
set -e
DEVELOPMENT_PATH='development';
DEVELOPMENT_ENV_PATH='development_env';
SCRIPT_NAME='preparing_setup.sh';
URL_FIRST_SCRIPT='https://raw.githubusercontent.com/juancarlosmiranda/shell_scripts_notes/main/preparing_setup.sh';
echo "Go to user home";
cd $HOME; 
echo "Create development";
mkdir -p $DEVELOPMENT_PATH;
cd $DEVELOPMENT_PATH; 
echo "Downloading development script";
wget $URL_FIRST_SCRIPT -O $SCRIPT_NAME
chmod 755 preparing_setup.sh; 
./$SCRIPT_NAME
