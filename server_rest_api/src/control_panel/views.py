"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:
"""

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.db import models

class NotImplementedYet(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        print('user:', request.user)
        print('request.META:', request.META)
        print('request.META[PATH_INFO]:', request.META['PATH_INFO'])

        content = {
            'status': status.HTTP_200_OK,
            'data': 'EXAMPLE_1'
        }
        return Response(content)

class UserData(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.auth
        user_id = kwargs['pk']
        print('request.user:', request.user)
        print('request.auth:', request.auth)
        print('kwargs[pk]:', kwargs['pk'])
        # TODO: NOT IMPLEMENTED YET
        content = {
            'status': status.HTTP_200_OK,
            'data': [
                {
                'id': 1,
                'email': 'an_email_here@server.com',
                'first_name': 'a_name_here',
                'last_name': 'a_lastname_here'
                }
            ]
        }
        return Response(content)

