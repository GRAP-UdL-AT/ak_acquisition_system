"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:

Use:

"""
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('login/', views.token),
    path('login/refresh/', views.refresh_token),
    path('logout/', views.logout_token),
]
