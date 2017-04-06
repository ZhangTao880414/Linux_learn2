# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOK', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter_article',
            name='Chapter_book',
            field=models.ForeignKey(verbose_name='\u4e66\u540d', blank=True, to='BOOK.book_info', null=True),
        ),
        migrations.AlterField(
            model_name='chapter_article',
            name='chapter_is_recommend',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u91cd\u70b9\u63a8\u8350'),
        ),
    ]
