"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from personal import views as personal_views
from django.urls import path, re_path, include
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import *

app_name='mysite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include('personal.urls', namespace = 'splash')),
    path('blog/', include('blog.urls', namespace = 'posts')),
    path('portfolio/', include('portfolio.urls', namespace = 'portfolio')),    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('myapi.urls', namespace='myapi')),
    path('api-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),   
    path('api-token-verify/', verify_jwt_token),    
     
]
handler404 = personal_views.error_404
handler500 = personal_views.error_500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)