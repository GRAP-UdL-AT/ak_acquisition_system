"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Description: This file contains tests for the API urls endpoints
Usage
    python3 manage.py test users.tests.tests_rest_api_endpoints

"""

from django.test import TestCase
import requests


class EndpointsTestCase(TestCase):
    """
    .
    """
    _user_name = 'user1'
    _user_pass = 'strong_pass1'
    # API ENDPOINTS urls
    _host_test = 'http://localhost:9000/'
    _api_rest_endpoint = 'v1/'
    _endpoint_register_user = 'authentication/register/'
    _endpoint_set_connection = 'authentication/login/'
    _endpoint_login_refresh = 'authentication/login/refresh/'
    _endpoint_finalize_connection = 'authentication/logout/'
    _endpoint_client_identification = _api_rest_endpoint + 'remote/'
    _endpoint_config_from_server = _api_rest_endpoint + 'config/'
    _endpoint_broadcast_cmd = _api_rest_endpoint + 'commands/'

    def setUp(self):
        """
        Settings
        # curl -d "username=user1&password=strong_pass1" http://localhost:9000/authentication/login/
        :return:
        """
        print('--- Setting test cases ---')
        endpoint = self._host_test + self._endpoint_set_connection
        data = {'username': self._user_name, 'password': self._user_pass}
        r = requests.post(endpoint, data=data).json()
        print('token --->' + r['access_token'])
        self.token = r['access_token']
        # ---------------------------------------
        pass

    # /register#
    def test_users_view_register(self):
        """
        Test register a user
        :return:
        """
        endpoint = self._host_test + self._endpoint_register_user
        data = {'username': self._user_name, 'password': self._user_pass}
        r = requests.post(endpoint, data=data).json()
        result_exist = r.get('username')[0]
        expected_str = 'A user with that username already exists.'
        self.assertEqual(expected_str, result_exist)

    # /commands/
    def test_command_view(self):
        """
        test command view
        :return:
        """
        print('test_commandView /commands/ -->')
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers)
        self.assertEqual(
            r.status_code,
            200, 'Status code, not equal to 200' + str(r.status_code)
        )

    def test_send_remote_cmd_enable_remote_client(self):
        """
        curl -H "Authorization: Bearer TOKEN_HERE" -d "command=ENABLE_REMOTE_CLIENT" http://localhost:9000/v1/commands/
        :return:
        """
        # ---------------------------------------
        # sending remote command
        remote_cmd_to_send = 'ENABLE_REMOTE_CLIENT'
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self.token}
        data = {'command': remote_cmd_to_send}
        r = requests.post(endpoint, data=data, headers=headers).json()
        # getting results
        result_pk_data_sent = r.get('data')[0]
        result_id_sent = result_pk_data_sent.get('pk')
        # ---------------------------------------
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers).json()
        result_id_cmd_query = r.get('id')
        result_cmd_query = r.get('command')
        # ---------------------------------------
        # checking responses
        self.assertEqual(result_id_sent, result_id_cmd_query, 'PK id is not equal')
        self.assertEqual(remote_cmd_to_send, result_cmd_query, 'COMMAND STR is not equal->' + remote_cmd_to_send)
        # ---------------------------------------

    # ------------------------------------
    # put here each command
    def test_send_remote_cmd_start(self):
        """
        curl -H "Authorization: Bearer TOKEN_HERE" -d "command=START_RECORD" http://localhost:9000/v1/commands/
        :return:
        """
        # ---------------------------------------
        # sending remote command
        remote_cmd_to_send = 'START_RECORD'
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self.token}
        data = {'command': remote_cmd_to_send}
        r = requests.post(endpoint, data=data, headers=headers).json()
        # getting results
        result_pk_data_sent = r.get('data')[0]
        result_id_sent = result_pk_data_sent.get('pk')
        # ---------------------------------------
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers).json()
        result_id_cmd_query = r.get('id')
        result_cmd_query = r.get('command')
        # ---------------------------------------
        # checking responses
        self.assertEqual(result_id_sent, result_id_cmd_query, 'PK id is not equal')
        self.assertEqual(remote_cmd_to_send, result_cmd_query, 'COMMAND STR is not equal->' + remote_cmd_to_send)
        # ---------------------------------------

    def test_send_remote_cmd_stop(self):
        """
        curl -H "Authorization: Bearer TOKEN_HERE" -d "command=STOP_RECORD" http://localhost:9000/v1/commands/
        :return:
        """
        # ---------------------------------------
        # sending remote command
        remote_cmd_to_send = 'STOP_RECORD'
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self.token}
        data = {'command': remote_cmd_to_send}
        r = requests.post(endpoint, data=data, headers=headers).json()
        # getting results
        result_pk_data_sent = r.get('data')[0]
        result_id_sent = result_pk_data_sent.get('pk')
        # ---------------------------------------
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers).json()
        result_id_cmd_query = r.get('id')
        result_cmd_query = r.get('command')
        # ---------------------------------------
        # checking responses
        self.assertEqual(result_id_sent, result_id_cmd_query, 'PK id is not equal')
        self.assertEqual(remote_cmd_to_send, result_cmd_query, 'COMMAND STR is not equal->' + remote_cmd_to_send)
        # ---------------------------------------

    def test_send_remote_cmd_waiting(self):
        """
        curl -H "Authorization: Bearer TOKEN_HERE" -d "command=WAITING" http://localhost:9000/v1/commands/
        :return:
        """
        # ---------------------------------------
        # sending remote command
        remote_cmd_to_send = 'WAITING'
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self.token}
        data = {'command': remote_cmd_to_send}
        r = requests.post(endpoint, data=data, headers=headers).json()
        # getting results
        result_pk_data_sent = r.get('data')[0]
        result_id_sent = result_pk_data_sent.get('pk')
        # ---------------------------------------
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers).json()
        result_id_cmd_query = r.get('id')
        result_cmd_query = r.get('command')
        # ---------------------------------------
        # checking responses
        self.assertEqual(result_id_sent, result_id_cmd_query, 'PK id is not equal')
        self.assertEqual(remote_cmd_to_send, result_cmd_query, 'COMMAND STR is not equal->' + remote_cmd_to_send)
        # ---------------------------------------

    def test_send_remote_cmd_stop_remote_client(self):
        """
        curl -H "Authorization: Bearer TOKEN_HERE" -d "command=STOP_REMOTE_CLIENT" http://localhost:9000/v1/commands/
        :return:
        """
        # ---------------------------------------
        # sending remote command
        remote_cmd_to_send = 'STOP_REMOTE_CLIENT'
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        headers = {'Authorization': 'Bearer ' + self.token}
        data = {'command': remote_cmd_to_send}
        r = requests.post(endpoint, data=data, headers=headers).json()
        # getting results
        result_pk_data_sent = r.get('data')[0]
        result_id_sent = result_pk_data_sent.get('pk')
        # ---------------------------------------
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = self._host_test + self._endpoint_broadcast_cmd
        r = requests.get(endpoint, headers=headers).json()
        result_id_cmd_query = r.get('id')
        result_cmd_query = r.get('command')
        # ---------------------------------------
        # checking responses
        self.assertEqual(result_id_sent, result_id_cmd_query, 'PK id is not equal')
        self.assertEqual(remote_cmd_to_send, result_cmd_query, 'COMMAND STR is not equal->' + remote_cmd_to_send)
        # ---------------------------------------

    def tearDown(self):
        """
        Clear all
        # curl -d "token=A_TOKEN_HERE" http://localhost:9000/authentication/logout/
        # curl -d "token=A_TOKEN_HERE" http://localhost:9000/authentication/token/revoke/
        :return:
        """
        print('--- Unsetting tokens ---', self.token)
        endpoint = self._host_test + self._endpoint_finalize_connection
        data = {'token': self.token}
        r = requests.post(endpoint, data=data).json()
