"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Class used to store host data, it is used in REST API CALLS

Use:
"""

class HostInfoRegister:
    uuid = None
    hostname = None
    os = None
    uptime_host = None
    ip_address_host = None
    uptime_remote_client = None
    mac_address = None
