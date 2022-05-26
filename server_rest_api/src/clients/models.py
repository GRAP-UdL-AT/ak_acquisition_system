"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:
"""

from django.db import models
import uuid

# Create your models here.

class RemoteClients(models.Model):
    """
    RemoteClients model
    """
    #uuid = models.UUIDField(default=uuid.uuid4)
    uuid = models.CharField(max_length=120)
    hostname = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    ip = models.CharField(max_length=16)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    # todo: add uptime
    # todo: add gps coords

    def __str__(self):
        return self.hostname


class BroadcastMessages(models.Model):
    """
    BroadcastMessages model
    """
    command = models.CharField(max_length=100)
    created = models.DateTimeField(null=True,)
    def __str__(self):
        return self.command


class BroadcastConfig(models.Model):
    """
    BroadcastConfig model
    """
    sleep_time = models.CharField(max_length=100)
    created = models.DateTimeField(null=True,)
    # todo: next config add as columns here
    def __str__(self):
        return self.sleep_time

# todo: add autonumerated fields, delete warnings