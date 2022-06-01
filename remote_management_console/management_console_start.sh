#/bin/bash!

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# software folders names
ROOT_FOLDER_NAME='ak_acquisition_system-main' 
REMOTE_MANAGEMENT_CONSOLE_NAME='remote_management_console'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/$ROOT_FOLDER_NAME/
REMOTE_MANAGEMENT_CONSOLE_F=$ROOT_FOLDER_F$REMOTE_MANAGEMENT_CONSOLE_NAME/


# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/$ROOT_FOLDER_NAME$ENV_NAME/
REMOTE_MANAGEMENT_CONSOLE_ENV_F=$ROOT_ENV_F$REMOTE_MANAGEMENT_CONSOLE_NAME$ENV_NAME/


# creating environments automatically
source $REMOTE_MANAGEMENT_CONSOLE_ENV_F$COMMON_ENV_PATH

python main_management_console.py
