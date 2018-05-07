from django.shortcuts import render
from blog import models as bModels
from portfolio import models as pModels
from rest_framework import generics
from myapi import serializers
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = bModels.Post.objects.active().order_by("-publish")
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class PostNewViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = bModels.Post.objects.active().order_by("-publish")
#         serializer_class = serializers.PostSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         queryset = bModels.Post.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer_class = serializers.PostSerializer(post)
#         return Response(serializer_class.data)

class PostNewViewSet(generics.ListCreateAPIView):
    queryset = bModels.Post.objects.active().order_by("-publish")
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save()

class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pModels.Portfolio.objects.active().order_by("-publish")
    serializer_class = serializers.PortfolioSerializer



# class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = pModels.Portfolio.objects.active().order_by("-publish")
#     serializer_class = serializers.PortfolioSerializer