from django.contrib import messages
from urllib.parse import quote_plus
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import (
						ListView, 
						DetailView, 
						CreateView, 
						UpdateView,
						DeleteView,
						)
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class PostList(LoginRequiredMixin, ListView):
	template_name	= "blog/post_list.html"
	
	def get_queryset(self):
		following = self.request.user.profile.following.all()

		following_ids = [i.id for i in following]

		queryset = Post.objects.filter(author__id__in = following_ids).order_by("-created_date")

		return queryset


	def post(self, request, *args, **kwargs):
		qs = User.objects.filter(username__icontains = request.POST.get("username"))

		following = self.request.user.profile.following.all()

		following_ids = [i.id for i in following]

		following_posts = Post.objects.filter(author__id__in = following_ids).order_by("-created_date")

		if not qs.exists():
			qs = -1

		context = {
			"queryset": qs,
			"object_list": following_posts,
		}

		return render(request, "blog/post_list.html", context)		


class PostDetail(DetailView):
	template_name = "blog/post_detail.html"
	queryset = Post.objects.all()	


class PostCreate(LoginRequiredMixin, CreateView):
	template_name = 'blog/post_create.html'
	form_class = PostForm
	success_url = "/blog"

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.author = self.request.user

		content = instance.text
		content = content.replace("<img", "<img class='img-fluid mx-auto d-block'")
		instance.text = content

		return super(PostCreate, self).form_valid(form)


	def get_success_url(self, *args, **kwargs):
		messages.success(self.request, "Post created successfully", extra_tags = 'created')
		return self.object.get_post_url()


class PostUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'blog/post_update.html'
	form_class = PostForm

	def get_queryset(self):
		queryset = Post.objects.filter(author = self.request.user)
		return queryset


	def get_success_url(self, *args, **kwargs):
		messages.success(self.request, "Post updated successfully", extra_tags = 'updated')
		return self.object.get_post_url()


class PostDelete(LoginRequiredMixin, DeleteView):
	model = Post

	def get_queryset(self):
		queryset = Post.objects.filter(author = self.request.user)
		return queryset


	def get_success_url(self, *args, **kwargs):
		messages.success(self.request, "Post deleted successfully", extra_tags = 'deleted')
		return self.object.get_absolute_url()