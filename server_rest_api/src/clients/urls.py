"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:
"""

from django.urls import path

from . import views

urlpatterns = [
    path('remote/', views.RemoteClientsViewSet.as_view()),
    path('commands/', views.CommandBroadcastList.as_view()),
    path('command/<int:pk>/', views.CommandByClient.as_view()),
    path('config/', views.ConfigRemoteClientsBroadcast.as_view())
]


