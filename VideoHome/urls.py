# -*- coding: utf-8 -*-
from django.conf.urls import url
from VideoHome.views import *
import logging
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.models import User
from models import *
from froms import  *
urlpatterns = [
    # url(r'^home/$', videohome, name='videohome'),
]
