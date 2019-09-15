from django.db import models

# Create your models here.
class Device(models.Model):
	device_name = models.CharField(max_length=50)
	status = models.BooleanField()
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.device_name