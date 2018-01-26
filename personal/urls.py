from django.urls import path, re_path, include
from . import views
from .forms import LoginForm

#patterns to link to poll/views.py

app_name = 'personal'

urlpatterns = [

	path('', views.index, name='index'),

	path('userlounge', views.userarea, name='lounge'),

	path('contact', views.contact, name='contact'),

	path('register', views.UserFormView.as_view(), name='register'),

	path('about', views.aboutView, name='about'),

	path('resume', views.resumeView, name='resume'),	

	path('login', views.LoginFormView.as_view(), name='login'),
 
 	path('logout', views.logoutView, name='logout'),



    ]
