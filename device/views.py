from django.shortcuts import render
from django.views.generic import ListView
from .models import Device

# Create your views here.
class ShowDevices(ListView):
	template_name = "device/device_list.html"
	queryset = Device.objects.all()

def fetch_device_data(request):
	template_name = "device/fetch.html"

	d = request.POST
	if d:
		if "dname" in d and "status" in d:
			d = Device(device_name=d.get("dname"), status=d.get("status"))
			d.save()
			print("Created")

	return render(request, template_name, {})