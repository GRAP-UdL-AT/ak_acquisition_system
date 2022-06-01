#!/bin/bash

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# software folders names
ROOT_FOLDER_NAME='ak_acquisition_system-main' 
SERVER_REST_API_NAME='server_rest_api'

# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/$ROOT_FOLDER_NAME$ENV_NAME/
SERVER_REST_API_ENV_F=$ROOT_ENV_F$SERVER_REST_API_NAME$ENV_NAME/
source $SERVER_REST_API_ENV_F$COMMON_ENV_PATH

python manage.py runserver 0:9000
deactivate
