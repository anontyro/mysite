from django.shortcuts import render
from blog import models as bModels
from portfolio import models as pModels
from myapi import serializers
from rest_framework import viewsets, permissions

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = bModels.Post.objects.active().order_by("-publish")
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pModels.Portfolio.objects.active().order_by("-publish")
    serializer_class = serializers.PortfolioSerializer