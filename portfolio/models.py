from django.db import models
from django.urls import reverse
from blog.storage import OverwriteStorage
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save #allows models to be altered before being saved
from django.utils.text import slugify
from blog.storage import OverwriteStorage

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Portfolio(models.Model):
	title = models.CharField(max_length=150)
	code = models.TextField()
	body = models.TextField()
	slug = models.SlugField(unique=True)
	draft = models.BooleanField(default = True)
	publish = models.DateField(default=timezone.now)
	date = models.DateTimeField(default=timezone.now)
	author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	tags = models.TextField()
	gitLink = models.URLField()
	image = models.FileField(default='/default.png', storage=OverwriteStorage())

	objects = PostManager()
	
	def get_absolute_url(self):
		return reverse('portfolio:view-portfolio',kwargs={'slug':self.slug}) #must give the views a name to correctly import as from urls(blog) the detailed url link

	def __str__(self):
		return self.title

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	slug = slugify(instance.title)
	exists = Portfolio.objects.filter(slug=slug).exists()
	if exists:
		slug = "%s-%s" %(slug, instance.id)
	instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Portfolio)