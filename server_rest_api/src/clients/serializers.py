"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:
"""

from rest_framework import serializers
from .models import RemoteClients
from .models import BroadcastMessages
from .models import BroadcastConfig

class RemoteClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteClients
        fields = '__all__'


class BroadcastMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastMessages
        fields = '__all__'


class BroadcastConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastConfig
        fields = '__all__'

