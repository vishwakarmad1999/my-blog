from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
	author 			= models.ForeignKey(User, on_delete = models.CASCADE)
	title 			= models.CharField(max_length = 60)
	text 			= models.TextField()
	created_date	= models.DateTimeField(auto_now_add = True)
	published_date	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title