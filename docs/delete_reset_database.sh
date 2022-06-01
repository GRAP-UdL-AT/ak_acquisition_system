#!/bin/bash
PYTHON="python"
echo $PYTHON

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# software folders names
ROOT_FOLDER_NAME='ak_acquisition_system-main' 
SERVER_REST_API_NAME='server_rest_api'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/$ROOT_FOLDER_NAME/
SERVER_REST_API_F=$ROOT_FOLDER_F$SERVER_REST_API_NAME/


# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/$ROOT_FOLDER_NAME$ENV_NAME/
SERVER_REST_API_ENV_F=$ROOT_ENV_F$SERVER_REST_API_NAME$ENV_NAME/
source $SERVER_REST_API_ENV_F$COMMON_ENV_PATH

echo "-------------------------------------"
echo "Deleting sqlite file"
echo "-------------------------------------"
find . -path "./db.sqlite3"  -delete

echo "-------------------------------------"
echo "Create a new DB"
echo "-------------------------------------"
python manage.py reset_db

echo "-------------------------------------"
echo "Cleaning old cache data"
echo "-------------------------------------"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*__pycache__*" -delete
echo "-------------------------------------"
echo "Creating migrations"
echo "-------------------------------------"
python manage.py makemigrations

echo "-------------------------------------"
echo "Applying migration to DB"
echo "-------------------------------------"
python manage.py migrate

echo "-------------------------------------"
echo "Adding pre-loaded values"
echo "-------------------------------------"
python manage.py loaddata $SERVER_REST_API_F'src/initial_data_values/group_values.json'
python manage.py loaddata $SERVER_REST_API_F'src/initial_data_values/users_values.json'
python manage.py loaddata $SERVER_REST_API_F'src/initial_data_values/oauth2_provider.json'
python manage.py loaddata $SERVER_REST_API_F'src/initial_data_values/broadcast_config.json'
python manage.py loaddata $SERVER_REST_API_F'src/initial_data_values/broadcast_messages.json'
# ----------------------------------------------------
# close virtual envoronment
deactivate
