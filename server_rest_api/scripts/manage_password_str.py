"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Script used to change passwords in users accounts
    This is used to put values in /src/initial_values/users_values.json

Usage:

    python ./manage.py runscript manage_password_str --chdir ./scripts/

Information sources:
    https://docs.djangoproject.com/en/3.2/topics/auth/passwords/
    https://stackoverflow.com/questions/17544537/django-pbkdf2-sha256-js-implementation

"""
from django.contrib.auth.hashers import make_password


class ManagePasswordStr(object):
    """
    .
    """

    def __init__(self, app_name):
        """
        .
        """
        self.app_name = app_name


def run():
    """
    .
    """
    print("This scripts helps to crete passwords strings!!->")
    print("Enter new password->")
    password_str = input()
    password_hash=make_password(password_str, salt=None, hasher='default')
    print("Copy text between || and paste into field password in /src/initial_data_values/users_values.json")
    print("Apply a reset DB with server_rest_db.sh")
    print(f"|{password_hash}|")

    pass
    # ------------------------------------------------------
