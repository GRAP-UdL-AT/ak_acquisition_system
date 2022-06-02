#!/bin/bash
# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# echo "Go to user home";cd $HOME; echo "create development";mkdir -p development;cd development; echo "Downloading development script";cp ./preparing_setup.sh ./development/; chmod 755 preparing_setup.sh; ./preparing_setup.sh

set -e

FILENAME_ZIP='ak_acquisition_system-main.zip'
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions
PYTHON_CMD='python3'
UNZIP_CMD=`which unzip`
MKDIR_CMD='mkdir -p'
CHMOD_CMD='chmod 755'

# files extensions names
EXT_SCRIPTS_SH='*.sh'
EXT_ZIP='.zip'

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'
SERVER_REST_API='server_rest_api_venv'
COMMON_ENV_PATH='bin/activate'


# software folders names
ROOT_FOLDER_NAME='ak_acquisition_system-main' 
REMOTE_CLIENT_AK_NAME='remote_client_ak'
REMOTE_CLIENT_GENERIC_NAME='remote_client_generic'
REMOTE_CLIENT_ZED_NAME='remote_client_zed'
REMOTE_MANAGEMENT_CONSOLE_NAME='remote_management_console'
SERVER_REST_API_NAME='server_rest_api'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/$ROOT_FOLDER_NAME/
REMOTE_CLIENT_AK_F=$ROOT_FOLDER_F$REMOTE_CLIENT_AK_NAME/
REMOTE_CLIENT_GENERIC_F=$ROOT_FOLDER_F$REMOTE_CLIENT_GENERIC_NAME/
REMOTE_CLIENT_ZED_F=$ROOT_FOLDER_F$REMOTE_CLIENT_ZED_NAME/
REMOTE_MANAGEMENT_CONSOLE_F=$ROOT_FOLDER_F$REMOTE_MANAGEMENT_CONSOLE_NAME/
SERVER_REST_API_F=$ROOT_FOLDER_F$SERVER_REST_API_NAME/


# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/$ROOT_FOLDER_NAME$ENV_NAME/
REMOTE_CLIENT_AK_ENV_F=$ROOT_ENV_F$REMOTE_CLIENT_AK_NAME$ENV_NAME/
REMOTE_CLIENT_GENERIC_ENV_F=$ROOT_ENV_F$REMOTE_CLIENT_GENERIC_NAME$ENV_NAME/
REMOTE_CLIENT_ZED_ENV_F=$ROOT_ENV_F$REMOTE_CLIENT_ZED_NAME$ENV_NAME/
REMOTE_MANAGEMENT_CONSOLE_ENV_F=$ROOT_ENV_F$REMOTE_MANAGEMENT_CONSOLE_NAME$ENV_NAME/
SERVER_REST_API_ENV_F=$ROOT_ENV_F$SERVER_REST_API_NAME$ENV_NAME/


# drawing
DRAW_LEVEL_0='|---'
DRAW_LEVEL_1='____|---'
DRAW_LEVEL_2='________|---/'
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

# decompress
$UNZIP_CMD -q $ROOT_FOLDER_NAME$EXT_ZIP

# draw software folder tree
echo "----------------------------"
echo "Software folder tree"
echo "----------------------------"

echo $DRAW_LEVEL_0$HOME
echo $DRAW_LEVEL_1$ROOT_FOLDER_F
echo $DRAW_LEVEL_2$REMOTE_CLIENT_AK_NAME
echo $DRAW_LEVEL_2$REMOTE_CLIENT_GENERIC_NAME
echo $DRAW_LEVEL_2$REMOTE_CLIENT_ZED_NAME
echo $DRAW_LEVEL_2$REMOTE_MANAGEMENT_CONSOLE_NAME
echo $DRAW_LEVEL_2$SERVER_REST_API_NAME

# draw software folder tree
echo "----------------------------"
echo "Virtual environment tree"
echo "----------------------------"
echo $DRAW_LEVEL_0$HOME
echo $DRAW_LEVEL_1$ROOT_ENV_F
echo $DRAW_LEVEL_2$REMOTE_CLIENT_AK_NAME$ENV_NAME
echo $DRAW_LEVEL_2$REMOTE_CLIENT_GENERIC_NAME$ENV_NAME
echo $DRAW_LEVEL_2$REMOTE_CLIENT_ZED_NAME$ENV_NAME
echo $DRAW_LEVEL_2$REMOTE_MANAGEMENT_CONSOLE_NAME$ENV_NAME
echo $DRAW_LEVEL_2$SERVER_REST_API_NAME$ENV_NAME



# change permissions in .sh
echo "-----------------------------------"
echo "Preparing permissions in *.sh files"
echo "-----------------------------------"
echo $CHMOD_CMD $REMOTE_CLIENT_AK_F$EXT_SCRIPTS_SH
echo $CHMOD_CMD $REMOTE_CLIENT_GENERIC_F$EXT_SCRIPTS_SH
echo $CHMOD_CMD $REMOTE_CLIENT_ZED_F$EXT_SCRIPTS_SH
echo $CHMOD_CMD $REMOTE_MANAGEMENT_CONSOLE_F$EXT_SCRIPTS_SH
echo $CHMOD_CMD $SERVER_REST_API_F$EXT_SCRIPTS_SH

#$CHMOD_CMD $REMOTE_CLIENT_AK_F$EXT_SCRIPTS_SH  # not suppported now
#$CHMOD_CMD $REMOTE_CLIENT_GENERIC_F$EXT_SCRIPTS_SH # not suppported now
$CHMOD_CMD $REMOTE_CLIENT_ZED_F$EXT_SCRIPTS_SH
#$CHMOD $REMOTE_MANAGEMENT_CONSOLE_F$EXT_SCRIPTS_SH # not suppported now
$CHMOD_CMD $SERVER_REST_API_F$EXT_SCRIPTS_SH


echo $ROOT_ENV_F
# create folder hierarchy
$MKDIR_CMD $ROOT_ENV_F



