from django.urls import path
from .views import UserPostView

app_name = 'user'

urlpatterns = [
	path('<str:username>/', UserPostView.as_view(), name = 'detail')
]