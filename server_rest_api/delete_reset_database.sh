#!/bin/sh
PYTHON="python"
echo $PYTHON

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda


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
python manage.py loaddata ./src/initial_data_values/group_values.json
python manage.py loaddata ./src/initial_data_values/users_values.json
python manage.py loaddata ./src/initial_data_values/oauth2_provider.json
python manage.py loaddata ./src/initial_data_values/broadcast_config.json
python manage.py loaddata ./src/initial_data_values/broadcast_messages.json
# ----------------------------------------------------

