# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 07:27:59 2019

@author: kmy07
"""

from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^handshake/(?P<data>[\w\-]+)', views.handshake),
]