# -*- coding: utf-8 -*-
from django.conf.urls import url
from VideoHome.views import *
urlpatterns = [
     url(r'^$', videohome, name='videohome'),
     url(r'^other$', other, name='other'),
     url(r'^video', video_category, name='video'),
]
