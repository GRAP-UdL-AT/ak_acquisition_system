"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
  A remote client to record videos from cameras hosted on different computers.

Use:
    python main_client_azure.py

"""


import logging
import os
import src.helpers.helper_path as hp
hp.kinect()
import src.helpers.helper_load_config as hc
from pyk4a import Config, ColorResolution, ImageFormat, DepthMode, FPS, WiredSyncMode
from time import gmtime
from src.remote_client_ak.remote_client_azure import RemoteClientAzure
from src.remote_client_ak.client_config import ClientConfig

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'remote_client.log')
    path_config_file = os.path.join(BASE_DIR, 'conf', 'client_settings.conf')
    path_conf_file_device_KA = os.path.join(BASE_DIR, 'conf', 'kinect_azure_settings.conf')
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime
    # todo: add check if device is not prepared close the app or raise and exception
    my_device_configuration=Config(
        color_resolution=ColorResolution.RES_720P,
        color_format=ImageFormat.COLOR_MJPG,
        depth_mode=DepthMode.NFOV_UNBINNED,
        camera_fps=FPS.FPS_30,
        synchronized_images_only=True,
        depth_delay_off_color_usec=0,
        wired_sync_mode=WiredSyncMode.STANDALONE,
        subordinate_delay_off_master_usec=0,
        disable_streaming_indicator=False
    )

    my_device_configuration = hc.load_config_from_file(path_conf_file_device_KA)
    # load default data, after configs are updated from server
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClientAzure(remote_config_obj, my_device_configuration)
    remote_obj.run()



