# coding:utf-8
from django.urls import path

from login import views

urlpatterns = [
    path('login.html', views.dologin)
]