# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views.generic.list import ListView
from blog.models import Post

def index(request):
    return render(request, 'blog/home.html')
def dashboard(request):
	usrname=request.user.username
	return ListView.as_view(queryset=Post.objects.filter(username=usrname).order_by("-date")[:25],template_name="blog/blog.html")(request)
# Create your views here.
