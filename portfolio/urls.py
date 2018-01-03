from django.urls import path, re_path, include
from django.views.generic import ListView, DeleteView, DetailView
from . import views

#patterns to link to poll/views.py

app_name = 'portfolio'

urlpatterns = [
	re_path(r'^$', views.Index.as_view(), name='portfolios'),

    re_path(r'add/$',views.PortfolioCreate.as_view(), name='add-portfolio'),

	re_path(r'^(?P<slug>[\w-]+)/$',views.DetailView.as_view(), name='view-portfolio'),

	re_path(r'^update/(?P<slug>[\w-]+)/$',views.PortfolioUpdate.as_view(), name='update-portfolio'),

	re_path(r'^delete/(?P<pk>[\d]+)/$',views.PortfolioDelete.as_view(), name='delete-portfolio')
    ]
