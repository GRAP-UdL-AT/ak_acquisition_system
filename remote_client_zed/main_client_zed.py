"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
  A remote client to record videos from cameras hosted on different computers.

Use:
    python client_main_zed.py

"""

import logging
import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'src'))
from time import gmtime
import helpers.helper_zed_load_config as hc
from remote_client_zed.client_config import ClientConfig
from remote_client_zed.remote_client_zed import RemoteClientZed

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'zed_thread_logger.log')
    path_config_file = os.path.join(BASE_DIR, 'conf', 'client_settings.conf')
    path_conf_file_zed = os.path.join(BASE_DIR, 'conf', 'zed_settings.conf')
    # Zed camera
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime

    my_zed_device_configuration = hc.load_zed_config_from_file(path_conf_file_zed)
    # load default data, after configs are updated from server
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClientZed(remote_config_obj, my_zed_device_configuration)
    remote_obj.run()
