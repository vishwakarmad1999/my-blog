from django.shortcuts import render
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


class PostList(ListView):
	template_name	= "blog/post_list.html"
	
	def get_queryset(self):
		queryset = Post.objects.order_by("-created_date")
		return queryset


class PostDetail(DetailView):
	template_name = "blog/post_detail.html"
	queryset = Post.objects.all()	


class PostCreate(LoginRequiredMixin, CreateView):
	template_name = 'blog/post_create.html'
	form_class = PostForm
	success_url = "/"

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