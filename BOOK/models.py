# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

# 书籍分类
class Book_Category(models.Model):
    Category_name = models.CharField(max_length=30, verbose_name='分类名称')
    Category_index = models.IntegerField(default=999, verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['Category_index', 'id']

    def __unicode__(self):
        return self.Category_name

# 书籍信息
class book_info(models.Model):
    book_name = models.CharField(max_length=50, verbose_name='书名')
    book_auth = models.CharField(max_length=50, verbose_name='作者')
    book_desc = models.CharField(max_length=120, verbose_name='书籍描述')
    book_is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    book_date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    book_category = models.ForeignKey(Book_Category, blank=True, null=True, verbose_name='分类')
    # objects = ArticleManager()

    class Meta:
        verbose_name = '书名'
        verbose_name_plural = verbose_name
        ordering = ['-book_date_publish']

    def __unicode__(self):
        return self.book_name

# 章节信息
class Chapter_Article(models.Model):
    Chapter_book=models.ForeignKey(book_info, blank=True, null=True, verbose_name='书名')
    chapter_title = models.CharField(max_length=50, verbose_name='章节标题')
    chapter_desc = models.CharField(max_length=120, verbose_name='章节简介')
    chapter_content = models.TextField(verbose_name='章节内容')
    chapter_is_recommend = models.BooleanField(default=False, verbose_name='是否重点推荐')
    chapter_date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # chapter_category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # chapter_tag = models.ManyToManyField(Tag, verbose_name='标签')
    # objects = ArticleManager()

    class Meta:
        verbose_name = '章节内容'
        verbose_name_plural = verbose_name
        ordering = ['-chapter_date_publish']
    def __unicode__(self):
        return self.chapter_title