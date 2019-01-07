from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import UserCreateForm
from .models import Profile

User = get_user_model()

# This file contains all the views necessary for rendering URLs

# UserCreate view is reponsible for creating a new user

class UserCreate(CreateView):
	form_class = UserCreateForm
	template_name = "templates/register.html"
	success_url = "/register-confirm"

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/')
		return super(UserCreate, self).dispatch(*args, **kwargs)


# HomeView acts as a landing for an authenticated user

class HomeView(LoginRequiredMixin, View):
	def get(self, request):
		template_name = 'templates/home.html'
		return render(request, template_name, {})


# This view is responsible for verify the activation key of a newly registered user

def verify_activation_key(request, key = None):
	if key:
		profile_obj = Profile.objects.filter(activation_key = key)
		if profile_obj.exists() and profile_obj.count() == 1:
			profile_obj = profile_obj.first()
			if profile_obj.activation_key == key:
				profile_obj.user.is_active = True
				profile_obj.user.save()
				return redirect('/login')
		raise Http404


# This view is rendered when the confirmation mail has been sent to the newly registered user

def register_confirm(request):
	template_name = "templates/register_confirm.html"
	return render(request, template_name, {})