from django.db import models
from django.conf import settings
from django.urls import reverse
from channel.models import Channel
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

class Post(models.Model):
	channel 		= models.ForeignKey(Channel, on_delete = models.CASCADE)
	author 			= models.ForeignKey(User, on_delete = models.CASCADE)
	title 			= models.CharField(max_length = 60)
	text 			= RichTextField()
	created_date	= models.DateTimeField(auto_now_add = True)
	published_date	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('user:detail', args=[self.author])


	def get_post_url(self):
		return reverse('blog:detail', args=[self.id])