from rest_framework import routers
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

app_name='myapi'

router = routers.SimpleRouter()
router.register(r'posts',views.PostViewSet)

urlpatterns = router.urls