#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from login import views

urlpatterns = [
    path("login", views.login),
]
