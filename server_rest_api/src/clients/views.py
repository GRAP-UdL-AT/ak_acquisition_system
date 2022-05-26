"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:
"""

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import permissions

from src.clients.models import RemoteClients
from src.clients.serializers import RemoteClientsSerializer

from src.clients.models import BroadcastMessages
from src.clients.serializers import BroadcastMessagesSerializer
from src.clients.models import BroadcastConfig
from src.clients.serializers import BroadcastConfigSerializer

from django.utils import timezone


class RemoteClientsViewSet(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    bad_request = {
        'status': status.HTTP_400_BAD_REQUEST,
        'data': [
            {
                'uuid': '',
            },
        ]
    }

    def get(self, request, format=None):
        queryset = RemoteClients.objects.all()
        serializer = RemoteClientsSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        if not (request.data.get('uuid')):
            return Response(self.bad_request, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('hostname')):
            return Response(self.bad_request, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('os')):
            return Response(self.bad_request, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('ip')):
            return Response(self.bad_request, status=status.HTTP_400_BAD_REQUEST)

        remote_clients_record = RemoteClients.objects.filter(hostname=request.data['hostname']).first()
        # check if exist
        if remote_clients_record:
            print('Client exist!')
            updated_field = timezone.now()
            remote_clients_record.updated = updated_field
            remote_clients_record.save()
            content = {
                'status': status.HTTP_200_OK,
                'data': [
                    {
                        'pk': remote_clients_record.pk,
                        'hostname': remote_clients_record.hostname,
                    },
                ]
            }
        else:
            print('Creating client')
            created_field = timezone.now()
            remote_clients_record = RemoteClients(uuid=request.data['uuid'], hostname=request.data['hostname'],
                                                  os=request.data['os'], ip=request.data['ip'], created=created_field)
            remote_clients_record.save()
            content = {
                'status': status.HTTP_201_CREATED,
                'data': [
                    {
                        'pk': remote_clients_record.pk,
                    },
                ]
            }
        return Response(content)


class CommandBroadcastList(APIView):
    """
    Manage broadcast messages to synchronize clients
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        search_record = BroadcastMessages.objects.order_by('created').last()
        serializer = BroadcastMessagesSerializer(search_record)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if not (request.data.get('command')):
            return Response(self.badrequest, status=status.HTTP_400_BAD_REQUEST)

        print(request.data['command'])
        print('Creating')
        created_field = timezone.now()
        broadcast_record = BroadcastMessages(command=request.data['command'], created=created_field)
        broadcast_record.save()
        content = {
            'status': status.HTTP_201_CREATED,
            'data': [
                {
                    'pk': broadcast_record.pk,
                },
            ]
        }
        # Example of a command
        # {"id":7,"command":"STOP_RECORDING","created":"2021-08-03T17:02:57.596946Z"}

        return Response(content)


class CommandByClient(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Get user data
        :param request:
        :return:
        """
        token = request.auth
        user_id = kwargs['pk']
        # -------------------------------------------
        print('-------------------------------------')
        print('request.user -->', request.user)
        print('request.auth -->', request.auth)
        print('Query params -->', kwargs['pk'])
        print('-------------------------------------')

        # -------------------------------------------
        # put code to search
        # -------------------------------------------
        content = {
            'status': 'request was PERMITTED User Profile view',
            'data': [
                {
                    'id': 1
                }
            ]
        }
        # -------------------------------------------
        return Response(content)
        # -------------------------------------------


class ConfigRemoteClientsBroadcast(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        print("GET config broadcast-->")
        search_record = BroadcastConfig.objects.order_by('created').last()
        serializer = BroadcastConfigSerializer(search_record)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print("POST config broadcast-->")
        if not (request.data.get('sleep_time')):
            return Response(self.badrequest, status=status.HTTP_400_BAD_REQUEST)

        # todo: check int values
        print(request.data['sleep_time'])
        created_field = timezone.now()
        broadcast_config_record = BroadcastConfig(sleep_time=request.data['sleep_time'], created=created_field)
        broadcast_config_record.save()
        content = {
            'status': status.HTTP_201_CREATED,
            'data': [
                {
                    'pk': broadcast_config_record.pk,
                },
            ]
        }
        return Response(content)

# TODO: update status
# TODO: get instruction
# TODO: inform log about completed instruction
# TODO: inform status changes
