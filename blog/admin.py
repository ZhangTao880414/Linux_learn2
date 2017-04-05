# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('username','password', 'desc', 'first_name', 'last_name', 'email', 'url', 'mobile', 'qq', 'avatar', 'is_staff', 'is_active')
        }),
    )

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('content', 'username', 'email', 'url', 'user', 'article',  'pid', )
        }),
    )
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad)