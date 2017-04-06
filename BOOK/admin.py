# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *
# Register your models here.
class book_infoAdmin(admin.ModelAdmin):
    list_display = ('book_category', 'book_name', 'book_auth', 'book_desc', 'book_is_recommend',)
    list_display_links = ('book_category', 'book_name', 'book_auth',)
    list_editable = ('book_is_recommend',)
    fieldsets = (
        (None, {
            'fields': ('book_name', 'book_desc','book_auth', 'book_is_recommend', 'book_category')
        }),
    )

class Chapter_ArticleAdmin(admin.ModelAdmin):
    list_display = ('Chapter_book', 'chapter_title',  'chapter_is_recommend',)
    list_display_links = ('Chapter_book', 'chapter_title',)
    list_editable = ('chapter_is_recommend',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(book_info, book_infoAdmin),
admin.site.register(Book_Category),
admin.site.register(Chapter_Article, Chapter_ArticleAdmin),
