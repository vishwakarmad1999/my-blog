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


class PostList(ListView):
	template_name	= "blog/post_list.html"
	
	def get_queryset(self):
		following = self.request.user.profile.following.all()

		following_ids = [i.id for i in following]

		queryset = Post.objects.filter(author__id__in = following_ids).order_by("-created_date")

		return queryset


	def post(self, request, *args, **kwargs):
		qs = User.objects.filter(username__icontains = request.POST['username'])

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
		print(form)
		instance = form.save(commit = False)
		instance.author = self.request.user
		return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'blog/post_update.html'
	form_class = PostForm
	success_url = "/blog"

	def get_queryset(self):
		queryset = Post.objects.filter(author = self.request.user)
		return queryset


class PostDelete(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = "/blog"

	def get_queryset(self):
		queryset = Post.objects.filter(author = self.request.user)
		return queryset