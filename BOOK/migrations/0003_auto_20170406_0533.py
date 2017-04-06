# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOK', '0002_auto_20170406_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_info',
            name='book_desc',
            field=models.CharField(max_length=120, verbose_name='\u4e66\u7c4d\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='chapter_article',
            name='chapter_desc',
            field=models.CharField(max_length=120, verbose_name='\u7ae0\u8282\u7b80\u4ecb'),
        ),
    ]
