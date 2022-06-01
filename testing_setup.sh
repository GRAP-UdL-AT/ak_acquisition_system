#!/bin/bash
# Decompress .zip

# mkdir development
# cd development
set -e
unzip -q ak_acquisition_system-main.zip

cd ak_acquisition_system-main

# ACTIVATE executables
chmod 755 ./server_rest_api/*.sh

# CREATING ENVIRONMENTS!
python3 -m venv $HOME/development_env/server_rest_api_venv
source $HOME/development_env/server_rest_api_venv/bin/activate


# UPDATE PIP
pip install --upgrade pip
pip install -r ./server_rest_api/requirements_linux.txt



#cd ./server_rest_api/
#./delete_reset_database.sh
#./rest_api_server_start.sh

