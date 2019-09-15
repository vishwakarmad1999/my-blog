from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from random import randint

# Create your models here.
class Channel(models.Model):
	admin 			= models.ForeignKey(User, on_delete=models.CASCADE)
	title 			= models.CharField(max_length=30)
	description 	= models.CharField(max_length=500)
	date_created	= models.DateField(auto_now_add=True)
	joined 			= models.ManyToManyField(User, related_name='joined', blank=True)
	slug 			= models.SlugField(blank=True)	 

	def __str__(self):
		return self.title


def channel_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		channel_obj = instance
		channels = Channel.objects.all()

		temp = instance.title.split()
		slug = ''

		for i in temp:
			slug += i.lower() + '-'
		slug = slug[:-1]

		for i in channels:
			if slug == i.slug:
				slug += '-' + str(randint(100000, 999999))
				break

		channel_obj.slug = slug
		channel_obj.save()


post_save.connect(channel_post_save_receiver, sender = Channel)