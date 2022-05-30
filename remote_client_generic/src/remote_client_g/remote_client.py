"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: This class contains code for remote client in a generic version. This receives commands from an API server.

Usage:
    remote_config_obj = ClientConfig(path_config_file)
    remote_obj = RemoteClient(remote_config_obj)
    remote_obj.run()

"""

import logging
import requests
import json
import time
import datetime
import socket
import sys
import os
import uuid
import configparser
from src.remote_client_g.cmd_config import CmdConfig
from src.remote_client_g.host_info_register import HostInfoRegister
from src.multithreading.job_thread_log import JobThreadLog

class RemoteClient:
    _remote_config = None
    _token = None
    _start_time_client = datetime.datetime.utcnow()
    _f_flag_config_name = os.path.join('conf', 'flag_first.ini')  #'./conf/flag_first.ini'
    # API ENDPOINTS urls
    _api_rest_endpoint = 'v1/'
    _endpoint_set_connection = 'authentication/login/'
    _endpoint_finalize_connection = 'authentication/logout/'
    _endpoint_client_identification = _api_rest_endpoint + 'remote/'
    _endpoint_config_from_server = _api_rest_endpoint + 'config/'
    _endpoint_broadcast_cmd = _api_rest_endpoint + 'commands/'
    # todo: refactor put here in configurable parameters all endpoints_url

    def __init__(self, config_param):
        logging.debug('STARTING REMOTE CLIENT')

        if config_param is None:
            logging.debug('config_param is empty')
        else:
            self._remote_config = config_param

    def __del__(self):
        logging.debug('STOPPING REMOTE CLIENT')

    def send_set_connection(self):
        logging.debug('set connection()')
        '''
        get token from server
        # curl -d 'username=my_user_str&password=my_pass' http://localhost:9000/authentication/login/
        :return:
        '''
        print('set_connection ()')
        # ---------------------------------------
        # To use this create user and password
        # ---------------------------------------
        endpoint_url = self._remote_config.url + '/' + self._endpoint_set_connection
        data = {'username': self._remote_config.user, 'password': self._remote_config.password}
        r = requests.post(endpoint_url, data=data).json()
        print('token --->' + r['access_token'])
        self._token = r['access_token']
        # ---------------------------------------

    def send_remote_client_identification(self, host_info_data_to_send):
        logging.debug('send_remote_client_identification')
        '''
        curl -H 'Authorization: Bearer TOKEN_HERE' -d 'uuid=12345&hostname=A_HOST&os='WINDOWS'&ip='192.168.0.1'' http://localhost:9000/v2/remote/
        :return:
        '''
        endpoint_url = self._remote_config.url + '/' + self._endpoint_client_identification
        headers = {'Authorization': 'Bearer ' + self._token}
        # todo: add uptime to API
        # todo:host_info_data_to_send.uptime_host
        # todo:host_info_data_to_send.uptime_remote_client
        data = {'uuid': host_info_data_to_send.uuid,
                'hostname': host_info_data_to_send.hostname,
                'os': host_info_data_to_send.os,
                'ip': host_info_data_to_send.ip_address_host
                }
        r = requests.post(endpoint_url, data=data, headers=headers).json()
        # ---------------------------------------

    def send_get_last_config_from_server(self):
        logging.debug('send_get_las_config_from_server')
        '''
        curl -H 'Authorization: Bearer TOKEN_HERE' http://localhost:9000/v2/config/
        curl -H 'Authorization: Bearer TOKEN_HERE' -d 'sleep_time=5' http://localhost:9000/v2/config/
        :return:
        '''
        endpoint_url = self._remote_config.url + '/' + self._endpoint_config_from_server
        headers = {'Authorization': 'Bearer ' + self._token}
        r = requests.get(endpoint_url, headers=headers)
        return r.status_code, r.text
        # ---------------------------------------

    def send_get_last_broadcast_cmd(self):
        logging.debug('get_last_broadcast_cmd')
        '''
        curl -H 'Authorization: Bearer TOKEN_HERE' http://localhost:9000/v2/commands/
        :return:
        '''
        endpoint_url = self._remote_config.url + '/' + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self._token}
        r = requests.get(endpoint_url, headers=headers)
        return r.status_code, r.text
        # ---------------------------------------

    def send_finalize_connection(self):
        logging.debug('finalize_connection()')
        '''
        logout from server, close connection
        # curl -d 'username=my_user_str&password=my_password_str' http://localhost:9000/authentication/logout/
        :return:
        '''
        print(f'finalize_connection ({self._token})')
        endpoint_url = self._remote_config.url + '/' + self._endpoint_finalize_connection
        data = {'token': self._token}
        r = requests.post(endpoint_url, data=data).json()
        # ---------------------------------------

    def get_execution_data(self):
        '''
        Returns execution data from this client
        :return:
        '''
        host_info_data = HostInfoRegister()
        host_info_data.os = sys.platform
        host_info_data.hostname = socket.getfqdn()
        host_info_data.ip_address_host = socket.gethostbyname(host_info_data.hostname)  # todo: check ip number
        host_info_data.uptime_remote_client = datetime.datetime.utcnow() - self._start_time_client

        return host_info_data

    def read_flag_config(self):
        '''
        Read conf from file client_settings.conf
        :return:
        '''
        f_config = configparser.ConfigParser()
        f_config.read(self._f_flag_config_name)
        uuid_host = f_config['DEFAULT']['uuid_host']
        return uuid_host

    def create_identity_data(self):
        '''
        Creates a unique identifier for this remote client
        Saves this identifier in a file
        If the file exists get data from this. If file not exists
        this is the first time execution, it must be calculated

        :return:
        '''
        uuid_remote_client = None

        if os.path.isfile(self._f_flag_config_name):
            logging.debug('Is not the first time, get uuid from file')
            uuid_remote_client = self.read_flag_config()
        else:
            # creates uuid flag in a file
            logging.debug('Is the first time, create UUID')
            uuid_remote_client = uuid.uuid1()
            flag_config = configparser.ConfigParser()
            flag_config['DEFAULT'] = {'uuid_host': uuid_remote_client}
            with open(self._f_flag_config_name, 'w') as flag_configfile:
                flag_config.write(flag_configfile)

        return str(uuid_remote_client)

    def run(self):
        '''
        Main process of the daemon, all operations step begin here
        :return:
        '''
        # ---------------------------------------------
        # INIT PARAMETERS
        # ---------------------------------------------
        # take note when the process start
        _start_time_client = datetime.datetime.utcnow()
        logging.debug('running...')
        self.send_set_connection()
        # get data from this computer client, load
        host_info_data_to_send = HostInfoRegister()
        host_info_data_to_send = self.get_execution_data()
        host_info_data_to_send.uuid = self.create_identity_data()
        self.send_remote_client_identification(host_info_data_to_send)
        # ---------------------------------------------
        # ---------------------------------------------
        # UPDATE PARAMETERS
        # ---------------------------------------------
        # load updates conf from central server
        config_server_result = self.send_get_last_config_from_server()
        code_status = config_server_result[0]
        text_res = config_server_result[1]
        response_dict = json.loads(text_res)
        self._remote_config.sleep_time = int(response_dict['sleep_time'])
        # ---------------------------------------------
        # todo:say hello and update table connection
        try:
            recording_flag = False
            while True:
                # ---------------------------------------------
                # check new commands from server
                # ---------------------------------------------
                command_result = self.send_get_last_broadcast_cmd()
                code_status = command_result[0]
                text_res = command_result[1]
                response_dict = json.loads(text_res)
                # todo:add here a check in error format
                command = response_dict['command']
                # ---------------------------------
                if command == CmdConfig.enable_remote_client:
                    print('Make something ENABLE')
                elif command == CmdConfig.start_record and (not recording_flag):
                    print('Make something START_RECORD')
                    logging.info('START_RECORD')
                    recording_flag = True
                    j1 = JobThreadLog()
                    j1.start()
                elif command == CmdConfig.stop_record and recording_flag:
                    print('Make something STOP_RECORD')
                    logging.info('STOP_RECORD')
                    recording_flag = False
                    j1.shutdown_flag.set()
                    j1.join()
                elif command == CmdConfig.waiting:
                    print('Make something WAITING')
                elif command == CmdConfig.take_capture:
                    print('TAKE A CAPTURE')
                elif command == CmdConfig.stop_remote_client:
                    print('CLOSE REMOTE PROCESS')
                    break
                else:
                    print('WAITING FOR ORDERS...')
                # ----------------------------------
                print(f'Sleeping a moment ... {self._remote_config.sleep_time} seconds')
                time.sleep(self._remote_config.sleep_time)
                # todo:update status with server
            ############################################
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            # close token
            self.send_finalize_connection()
            exit(1)
        # ---------------------------------------------
        # close token, close connection
        # ---------------------------------------------
        self.send_finalize_connection()
        # ---------------------------------------------

    def run_test(self):
        # TODO: DELETE THIS METHOD
        # ---------------------------------------------
        # INIT PARAMETERS
        # ---------------------------------------------
        # take note when the process start
        _start_time_client = datetime.datetime.utcnow()
        logging.debug('run()')
        self.send_set_connection()
        # get data from this computer client, load
        host_info_data_to_send = HostInfoRegister()
        host_info_data_to_send = self.get_execution_data()
        host_info_data_to_send.uuid = self.create_identity_data()
        self.send_remote_client_identification(host_info_data_to_send)
        # ---------------------------------------------
        # ---------------------------------------------
        # UPDATE PARAMETERS
        # ---------------------------------------------
        # load updates conf from central server
        config_server_result = self.send_get_last_config_from_server()
        code_status = config_server_result[0]
        text_res = config_server_result[1]
        response_dict = json.loads(text_res)
        self._remote_config.sleep_time = int(response_dict['sleep_time'])
        # ---------------------------------------------

        # -------------------
        # while some stuff here
        # -------------------
        print('while some stuff here ->')
        # ---------------------------------------------
        # close token, close connection
        # ---------------------------------------------
        self.send_finalize_connection()
        # ---------------------------------------------
