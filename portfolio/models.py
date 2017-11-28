from django.db import models
from blog.storage import OverwriteStorage
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save #allows models to be altered before being saved

class Portfolio(models.Model):
	title = models.CharField(max_length=150)
	code = models.TextField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=150)
	tags = models.TextField()
	gitLink = models.URLField()
	image = models.FileField(default='/media/default.png', storage=OverwriteStorage())

	def __str__(self):
		return self.title

