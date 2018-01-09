from rest_framework import serializers
from blog import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('title', 'body', 'slug','date','draft','publish','author', 'cover_img')



    # title = serializers.CharField(max_length = 140)
    # body = serializers.TimeField()
    # slug = serializers.SlugField()
    # date = serializers.DateTimeField()
    # draft = serializers.BooleanField()
    # publish = serializers.DateField()
    # cover_img = serializers.FileField()