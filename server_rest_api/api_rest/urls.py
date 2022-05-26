"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Django configurations
"""

from django.urls import path
from django.urls import include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api_rest.settings import REST_API_ROOT

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('src.users.urls')),
    path('api_rest/', include(router.urls)),
    path(REST_API_ROOT, include('src.control_panel.urls')),
    path(REST_API_ROOT, include('src.clients.urls')),
]
