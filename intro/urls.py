# coding:utf-8
from django.urls import path

from intro import views

urlpatterns = [
    path('intro', views.index)
]


