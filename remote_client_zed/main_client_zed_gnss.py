"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    A remote client to record videos from cameras hosted on different computers.
    This is an special client with access to Zed camera and GNSS Ardu simple

Use:
    python client_main_zed_gnss.py

"""

import logging
import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'src'))
from time import gmtime
import src.helpers.helper_zed_load_config as hc
from src.remote_client_classes.client_config import ClientConfig
from src.remote_client_classes.remote_client_zed_gnss import RemoteClientZedGNSS
from src.gnss_classes.gnss_config import GNSSConfig

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    # general configs
    path_client_log_file = os.path.join(BASE_DIR, 'log', 'zed_thread_logger.log')
    path_client_config_file = os.path.join(BASE_DIR, 'conf', 'client_settings.conf')
    # Zed camera
    path_camera_conf_file_zed = os.path.join(BASE_DIR, 'conf', 'zed_settings.conf')
    # Ardusimple config
    path_gnss_config_file = os.path.join(BASE_DIR, 'conf', 'gnss_settings.conf')
    path_gnss_output_file = os.path.join(BASE_DIR, 'recorded_gnss', '_GNSS_GGA_track.txt')

    # check if is enabled gnsss
    # check if is enabled Zed
    # if all is ok go to process
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_client_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime

    # get device config
    my_zed_device_configuration = hc.load_zed_config_from_file(path_camera_conf_file_zed)
    my_gnss_device_configuration = GNSSConfig(path_gnss_config_file)

    # load default data, after configs are updated from server
    remote_zed_gnss_config_obj = ClientConfig(path_client_config_file)
    remote_client_zed_gnss_obj = RemoteClientZedGNSS(remote_zed_gnss_config_obj, my_zed_device_configuration,
                                                     my_gnss_device_configuration)
    remote_client_zed_gnss_obj.run()

# todo. add checks is bad functions or errors
# todo: put in a config for remote and add inheritance
# todo: add utc time
