from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save
from .utils import random_string_generator
from django.core.mail import send_mail

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
	def toggle_follow(self, request_user, profile_user):
		is_following = profile_user in request_user.profile.following.all()
		if is_following:
			request_user.profile.following.remove(profile_user)
		else:
			request_user.profile.following.add(profile_user)


# This is the model used in the backend to verify a user by using a activation mail
 
class Profile(models.Model):
	user 			= models.OneToOneField(User, on_delete = models.CASCADE)
	activation_key	= models.CharField(max_length = 30, null = True, blank = True)
	following 		= models.ManyToManyField(User, related_name = 'followers')

	objects = ProfileManager()

	def send_activation_mail(self):
		send_mail(
	    'Verify yourself',
	    'Dear ' + self.user.username + '\nGo to this link: vishwakarmad1999.pythonanywhere.com/activate/' + self.activation_key,
	    '',
	    [self.user.email],
	    fail_silently=False,
	    )

	
	def __str__(self):
		return str(self.user)	


def user_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		profile_obj = Profile(user = instance)
		profile_obj.activation_key = random_string_generator(30)
		profile_obj.save()

post_save.connect(user_post_save_receiver, sender = User)