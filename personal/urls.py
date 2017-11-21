from django.conf.urls import url, include
from . import views
from .forms import LoginForm

#patterns to link to poll/views.py

app_name = 'personal'

urlpatterns = [

	url(r'^$', views.index, name='index'),

	url(r'^userlounge/$', views.userarea, name='lounge'),

	url(r'^contact/$', views.contact, name='contact'),

	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	url(r'^about/$', views.aboutView, name='about'),

	url(r'^login/$', views.LoginFormView.as_view(), name='login'),
 
 	url(r'^logout/$', views.logoutView, name='logout'),



    ]
