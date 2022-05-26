"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:

"""

import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import CreateUserSerializer
from api_rest.settings import REST_API_SERVICE_URL, CLIENT_IDENTIFIER_STR, CLIENT_SECRET


@permission_classes([AllowAny])
class UserRegister(APIView):
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            r = requests.post('http://127.0.0.1:9000/o/token/',
                              data={
                                  'grant_type': 'password',
                                  'username': request.data['username'],
                                  'password': request.data['password'],
                                  'client_id': CLIENT_IDENTIFIER_STR,
                                  'client_secret': CLIENT_SECRET,
                              },
                              )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post(REST_API_SERVICE_URL + '/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['username'],
                              'password': request.data['password'],
                              'client_id': CLIENT_IDENTIFIER_STR,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post(
        REST_API_SERVICE_URL + '/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_IDENTIFIER_STR,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post(
        REST_API_SERVICE_URL + '/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_IDENTIFIER_STR,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def logout_token(request):
    r = requests.post(
        REST_API_SERVICE_URL + '/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_IDENTIFIER_STR,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    return Response(r.json(), r.status_code)
