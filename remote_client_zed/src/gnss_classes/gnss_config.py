"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: This class contains special options to configure a GNSS Ardu Simple

Use:
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClient(remote_config_obj)
    remote_obj.run()

"""


import logging
import configparser
import os


class GNSSConfig:
    serial_port_master = None
    serial_port_alternative = None
    baudrate = None
    BASE_DIR = os.path.abspath('.')
    f_config_name = os.path.join(BASE_DIR, 'conf', 'gnss_settings.conf')
    path_gnss_output_file = os.path.join(BASE_DIR, 'recorded_gnss')
    file_name = '_GNSS_GGA_track.txt'

    def __init__(self, file_config=None):
        logging.debug('Constructor GNSSConfig()')
        if file_config is None:
            logging.debug('Load default settings!')
            # todo. add checking for other operating systems
            self.set_default()
        else:
            logging.debug('Load settings from file')
            if os.path.isfile(file_config):
                self.read_config()
            else:
                logging.debug('Load default settings, file not found!')
                self.set_default()

    def set_default(self):
        self.serial_port_master = '/dev/ttyACM0'
        self.serial_port_alternative = '/dev/ttyACM1'
        self.baudrate = 115200

    def read_config(self):
        """
        Read config from file gnss_settings.conf
        :return:
        """
        f_config = configparser.ConfigParser()
        f_config.read(self.f_config_name)
        self.serial_port_master = f_config['DEFAULT']['serial_port_master']
        self.serial_port_alternative = f_config['DEFAULT']['serial_port_alternative']
        self.baudrate = f_config['DEFAULT']['baudrate']
        self.path_gnss_output_file = f_config['DEFAULT']['path_gnss_output_file']

    def __del__(self):
        logging.debug('Finalize GNSSConfig()')
