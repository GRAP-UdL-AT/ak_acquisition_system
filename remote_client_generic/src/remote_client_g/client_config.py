"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: This class contains special options to configure a remote client.

Usage:
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClient(remote_config_obj)
    remote_obj.run()

"""

import logging
import configparser
import os
from enum import IntEnum


class STATUS(IntEnum):
    BEGIN = 0
    WAITING = 1
    END = 2


class ClientConfig:
    protocol = None
    host = None
    port = None
    user = None
    password = None
    sleep_time = None
    f_config_name = None  # os.path.join('../', 'conf', 'client_settings.conf')

    def __init__(self, file_config, protocol=None, host=None, port=None, user=None, password=None, sleep_time=5):
        logging.debug('Constructor ClientConfig()')
        if os.path.isfile(file_config):
            logging.debug('Load conf from file')
            self.f_config_name = file_config
            self.read_config()
        else:
            logging.debug('Load default conf')
            self.protocol = 'http'
            self.host = '127.0.0.1'
            self.port = '9000'
            self.user = ''
            self.password = ''
            self.sleep_time = 5
        # ---------------------------------
        self.url = self.protocol + '://' + self.host + ':' + self.port
        logging.debug('user=' + self.user)
        logging.debug('user=' + self.password)
        logging.debug('user=' + self.url)

    def read_config(self):
        """
        Read conf from file client_settings.conf
        :return:
        """
        f_config = configparser.ConfigParser()
        # by default from client_settings.conf
        f_config.read(self.f_config_name)
        self.protocol = f_config['DEFAULT']['protocol']
        self.host = f_config['DEFAULT']['host']
        self.port = f_config['DEFAULT']['port']
        self.user = f_config['DEFAULT']['user']
        self.password = f_config['DEFAULT']['password']
        self.sleep_time = int(f_config['DEFAULT']['sleep_time'])


    def __del__(self):
        logging.debug('Finalize ClientConfig()')
