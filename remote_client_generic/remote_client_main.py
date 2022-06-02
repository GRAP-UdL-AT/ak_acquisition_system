"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: Main process, which executes routines. This requires the API server to be active

Use:
    python remote_client_main.py
"""


import logging
import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'src'))
from src.remote_client_g.remote_client import RemoteClient
from src.remote_client_g.client_config import ClientConfig

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'remote_client.log')
    path_config_file = os.path.join(BASE_DIR, 'conf', 'client_settings.conf')

    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    # load default data, after configs are updated from server
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClient(remote_config_obj)
    remote_obj.run()

    # OPTIONAL
    # todo: add inheritance for other types of daemons
    # all: make threads.
    # all: add remote capture

    # API server
    # todo: add remote conf from API, update sleep value
    # all: add TASK EXECUTED / completed book

    # remote client generic
    # todo: add script to automatize folder creation

    # UI MANAGER
    # TODO: add users for UI
    # todo: handle exceptions when is not connection

    # TESTING
    # todo: add test to functions
    # all: use data directory for windows
    # all: test the installation process on Windows and Linux
    # todo: add hot configuration