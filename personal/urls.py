from django.urls import path, re_path, include
from . import views
from .forms import LoginForm

#patterns to link to poll/views.py

app_name = 'personal'

urlpatterns = [

	re_path(r'^$', views.index, name='index'),

	re_path(r'^userlounge/$', views.userarea, name='lounge'),

	re_path(r'^contact/$', views.contact, name='contact'),

	re_path(r'^register/$', views.UserFormView.as_view(), name='register'),

	re_path(r'^about/$', views.aboutView, name='about'),

	path('login', views.LoginFormView.as_view(), name='login'),
 
 	re_path(r'^logout/$', views.logoutView, name='logout'),



    ]
