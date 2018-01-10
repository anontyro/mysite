from rest_framework import serializers
from portfolio import models as pModel
from blog import models as bModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = bModel.Post
        fields = ('title', 'body', 'slug','date','draft','publish','author', 'cover_img')

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = pModel.Portfolio
        fields = ('title', 'code', 'body', 'slug', 'draft', 'publish', 'date', 'author', 'tags', 'gitLink', 'image')

    # title = serializers.CharField(max_length = 140)
    # body = serializers.TimeField()
    # slug = serializers.SlugField()
    # date = serializers.DateTimeField()
    # draft = serializers.BooleanField()
    # publish = serializers.DateField()
    # cover_img = serializers.FileField()