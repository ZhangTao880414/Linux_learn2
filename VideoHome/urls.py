# -*- coding: utf-8 -*-
from django.conf.urls import url
from VideoHome.views import *
urlpatterns = [
     url(r'^$', videohome, name='videohome'),
]
