from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Channel
from blog.models import Post
from .forms import ChannelForm

# Create your views here.
class ChannelDetailView(DetailView):
	template_name = "channel/channel_detail.html"
	queryset = Channel.objects.all()

	def get_context_data(self, **kwargs):
	    context = super(ChannelDetailView, self).get_context_data(**kwargs)
	    
	    context['joined'] = context['object'].joined.all()
	    if self.request.user.is_authenticated:
	    	context['is_joined'] = self.request.user in context['joined']

	    context['posts'] = Post.objects.filter(channel = context['object']).order_by("-created_date")

	    return context


	def post(self, request, *args, **kwargs):
		request_user = request.user
		channel_obj = Channel.objects.get(slug = kwargs['slug'])

		is_joined = request_user in channel_obj.joined.all()

		if is_joined:
			channel_obj.joined.remove(request_user)
		else:
			channel_obj.joined.add(request_user)

		return redirect("/c/" + kwargs['slug'])


class ChannelCreateView(LoginRequiredMixin, CreateView):
	template_name = "channel/channel_create.html"
	form_class = ChannelForm
	success_url = "/blog"

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.admin = self.request.user

		return super(ChannelCreateView, self).form_valid(form)


class ChannelListView(LoginRequiredMixin, ListView):
	template_name = "channel/channel_list.html"
	queryset = Channel.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ChannelListView, self).get_context_data(*args, **kwargs)
		queryset = Channel.objects.filter(joined = self.request.user)
		context['qs'] = queryset
		return context