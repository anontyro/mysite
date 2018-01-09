from django.shortcuts import render
from blog import models
from myapi import serializers
from rest_framework import viewsets

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer