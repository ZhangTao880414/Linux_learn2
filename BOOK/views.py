# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# Create your views here.

#分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 2)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

def get_chapter(request):
    book_list = book_info.objects.all()
    cid = request.GET.get('cid', None)
    print cid
    Chapter_content = Chapter_Article.objects.filter(pk=cid)
    Chapter_content = getPage(request, Chapter_content)
     # print Chapter_content
    return render(request, 'BookHome2.html', locals())


def get_book(request):
    try:
        book_list = book_info.objects.filter(book_display=1)
        book_id = request.GET.get('book_id', None)
        Chapter_id = request.GET.get('cid', None)

        # 设置文章默认展示书籍
        if book_id is None:
            book_id = 1
        # 通过书籍id找到书籍第一页
        if Chapter_id is None:
            Chapter_id = Chapter_Article.objects.get(Chapter_book_id=book_id, Chapter_level=1).id
        try:
            book_name = book_info.objects.get(pk=book_id)
            Chapter_name = Chapter_Article.objects.get(pk=Chapter_id)
        except book_info.DoesNotExist:
            pass

        Chapter_Title_list = Chapter_Article.objects.filter(Chapter_book=book_name,chapter_display=1).order_by('Chapter_level')
    except Exception as e:
        pass
    return render(request, 'BookHome.html', locals())