# -*- coding: utf-8 -*-
from django.conf.urls import url
from BOOK.views import *

urlpatterns = [
    # url(r'^logout$', do_logout, name='logout'),
    # url(r'^reg', do_reg, name='reg'),
    url(r'^chapter/$', get_chapter, name='get_chapter'),
    url(r'^/$', get_book, name='get_book'),
]
