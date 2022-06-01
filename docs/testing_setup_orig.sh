#!/bin/bash
# Decompress .zip

FILENAME_ZIP='ak_acquisition_system-main.zip'
REQUERIMENTS_LINUX='requirements_linux.txt'
PYTHON_CMD='python3'
UNZIP_CMD=`which unzip`
CHMOD='chmod 755'


DEVELOPMENT_ENV_PATH='development_env'
SERVER_REST_API='server_rest_api_venv'
COMMON_ENV_PATH='bin/activate'
EXT_SCRIPTS_SH='*.sh'
EXT_ZIP='.zip'

# software folders
ROOT_FOLDER_F='ak_acquisition_system-main' 
REMOTE_CLIENT_F='remote_client_ak'
REMOTE_CLIENT_GENERIC_F='remote_client_generic'
REMOTE_CLIENT_ZED_F='remote_client_zed'
REMOTE_MANAGEMENT_CONSOLE_F='remote_management_console'
SERVER_REST_API_F='server_rest_api'

# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$ROOT_FOLDER_F$ENV_NAME
REMOTE_CLIENT_ENV_F=$REMOTE_CLIENT_F$ENV_NAME
REMOTE_CLIENT_GENERIC_ENV_F=$REMOTE_CLIENT_GENERIC_F$ENV_NAME
REMOTE_CLIENT_ZED_ENV_F=$REMOTE_CLIENT_ZED_F$ENV_NAME
REMOTE_MANAGEMENT_CONSOLE_ENV_F=$REMOTE_MANAGEMENT_CONSOLE_F$ENV_NAME
SERVER_REST_API_ENV_F=$SERVER_REST_API_F$ENV_NAME



# software directories
#|---\ak_acquisition_system-main
#	|---\remote_client_ak
#	|---\remote_client_generic
#	|---\remote_client_zed
#	|---\remote_management_console
#	|---\server_rest_api

# development environment
#|---\ak_acquisition_system-main_venv
#	|---\remote_client_ak_venv
#	|---\remote_client_generic_venv
#	|---\remote_client_zed_venv
#	|---\remote_management_console_venv
#	|---\server_rest_api_venv




# mkdir development
# cd development
set -e
#unzip -q ak_acquisition_system-main.zip
unzip -q $ROOT_FOLDER_F$EXT_ZIP

cd $ROOT_FOLDER_F
cd ak_acquisition_system-main

# ACTIVATE executables
#chmod 755 ./server_rest_api/*.sh

# CREATING ENVIRONMENTS!
#python3 -m venv $HOME/development_env/server_rest_api_venv
#source $HOME/development_env/server_rest_api_venv/bin/activate


# UPDATE PIP
#pip install --upgrade pip
#pip install -r ./server_rest_api/requirements_linux.txt



#cd ./server_rest_api/
#./delete_reset_database.sh
#./rest_api_server_start.sh

