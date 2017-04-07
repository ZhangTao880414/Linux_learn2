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
        book_list = book_info.objects.all()
        book_id = request.GET.get('book_id', None)
        # print cid
        try:
            book_name = book_info.objects.get(pk=book_id)
            # print book
        except book_info.DoesNotExist:
            # return render(request, 'failure.html', {'reason': '分类不存在'})
            pass
        Chapter_list = Chapter_Article.objects.filter(Chapter_book=book_name).order_by('Chapter_level')
        # print Chapter_Article_list
        Chapter_list = getPage(request, Chapter_list)
    except Exception as e:
        pass
    return render(request, 'BookHome.html', locals())