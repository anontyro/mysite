from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

app_name='myapi'