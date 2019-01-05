from django.shortcuts import render
from django.http import Http404
# from django.views.generic import ListView

def post_list(request):
	return render(request, "blog/post_list.html", {})