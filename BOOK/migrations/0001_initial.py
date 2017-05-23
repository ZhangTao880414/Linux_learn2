# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category_name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('Category_index', models.IntegerField(default=999, verbose_name='\u5206\u7c7b\u7684\u6392\u5e8f')),
            ],
            options={
                'ordering': ['Category_index', 'id'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='book_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=50, verbose_name='\u4e66\u540d')),
                ('book_auth', models.CharField(max_length=50, verbose_name='\u4f5c\u8005')),
                ('book_desc', models.CharField(max_length=300, verbose_name='\u4e66\u7c4d\u63cf\u8ff0')),
                ('book_is_recommend', models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350')),
                ('book_date_publish', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('book_display', models.BooleanField(default=False, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('book_category', models.ForeignKey(verbose_name='\u5206\u7c7b', blank=True, to='BOOK.Book_Category', null=True)),
            ],
            options={
                'ordering': ['book_category', '-book_date_publish'],
                'verbose_name': '\u4e66\u540d',
                'verbose_name_plural': '\u4e66\u540d',
            },
        ),
        migrations.CreateModel(
            name='Chapter_Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Chapter_level', models.FloatField(default='1', max_length=10, verbose_name='\u7ea7\u522b')),
                ('chapter_title', models.CharField(max_length=50, verbose_name='\u7ae0\u8282\u6807\u9898')),
                ('chapter_desc', models.CharField(max_length=300, verbose_name='\u7ae0\u8282\u7b80\u4ecb')),
                ('chapter_content', models.TextField(verbose_name='\u7ae0\u8282\u5185\u5bb9')),
                ('chapter_is_recommend', models.BooleanField(default=False, verbose_name='\u662f\u5426\u91cd\u70b9\u63a8\u8350')),
                ('chapter_display', models.BooleanField(default=False, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('chapter_date_publish', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('Chapter_book', models.ForeignKey(verbose_name='\u4e66\u540d', blank=True, to='BOOK.book_info', null=True)),
            ],
            options={
                'ordering': ['Chapter_book', 'Chapter_level'],
                'verbose_name': '\u7ae0\u8282\u5185\u5bb9',
                'verbose_name_plural': '\u7ae0\u8282\u5185\u5bb9',
            },
        ),
    ]
