"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Manage connections between management console and central server. Messages connections
    are implemented here.

Use:

        ui_config_obj = UIClientConfig()
        connection_obj = RemoteConnection(ui_config_obj)

"""
import requests


# Could be implemented with inheritance
class RemoteConnection:
    _ui_client_config = None
    _token = None
    _last_cmd_from_server = None
    # API ENDPOINTS urls
    _api_rest_endpoint = 'v1/'
    _endpoint_set_connection = 'authentication/login/'
    _endpoint_finalize_connection = 'authentication/logout/'
    _endpoint_cmd_remote = _api_rest_endpoint + 'commands/'
    # _endpoint_config_from_server = _api_rest_endpoint + 'config/'
    endpoint_broadcast_cmd = _api_rest_endpoint + 'commands/'

    X_MESSAGE = 1
    Y_MESSAGE = 1

    def __init__(self, config_param):
        if config_param is None:
            print('config_param is empty')
        else:
            self._ui_client_config = config_param

    def send_set_connection(self):
        """
        get token from server
        # curl -d 'username=my_user_str&password=my_pass' http://localhost:9000/authentication/token/
        :return:
        """
        # print('set_connection ()')
        # ---------------------------------------
        # To use this create user and password
        # ---------------------------------------
        endpoint_url = self._ui_client_config.url + '/' + self._endpoint_set_connection
        data = {'username': self._ui_client_config.user, 'password': self._ui_client_config.password}
        r = requests.post(endpoint_url, data=data).json()
        # print('token --->' + r['access_token'])
        self._token = r['access_token']
        # ---------------------------------------

    def send_remote_cmd(self, remote_cmd_str):
        """
        curl -H 'Authorization: Bearer TOKEN_HERE' -d 'uuid=12345&hostname=A_HOST&os='WINDOWS'&ip='192.168.0.1'' http://localhost:9000/v2/remote/
        :return:
        """
        endpoint_url = self._ui_client_config.url + '/' + self._endpoint_cmd_remote
        headers = {'Authorization': 'Bearer ' + self._token}
        # todo: add uptime to API
        # todo:host_info_data_to_send.uptime_host
        # todo:host_info_data_to_send.uptime_remote_client
        data = {'command': remote_cmd_str}
        r = requests.post(endpoint_url, data=data, headers=headers).json()
        # ---------------------------------------

    def send_get_last_broadcast_cmd(self):
        """
        curl -H 'Authorization: Bearer TOKEN_HERE' http://localhost:9000/v2/commands/
        :return:
        """
        endpoint_url = self._ui_client_config.url + '/' + self._endpoint_cmd_remote
        headers = {'Authorization': 'Bearer ' + self._token}
        r = requests.get(endpoint_url, headers=headers)
        return r.status_code, r.text
        # ---------------------------------------

    def send_finalize_connection(self):
        """
        logout from server, close connection
        # curl -d 'username=my_user_str&password=my_password_str' http://localhost:9000/authentication/token/logout/
        :return:
        """
        # print(f'finalize_connection ({self._token})')
        endpoint_url = self._ui_client_config.url + '/' + self._endpoint_finalize_connection
        data = {'token': self._token}
        r = requests.post(endpoint_url, data=data).json()
