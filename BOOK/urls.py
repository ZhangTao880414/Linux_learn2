# -*- coding: utf-8 -*-
from django.conf.urls import url
from BOOK.views import *

urlpatterns = [

    url(r'^chapter/$', get_chapter, name='get_chapter'),
    url(r'^/$', get_book, name='get_book'),
]
