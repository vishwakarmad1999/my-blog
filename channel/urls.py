from django.urls import path
from .views import ChannelDetailView, ChannelCreateView, ChannelListView

app_name = 'channel'


urlpatterns = [
	path('list/', ChannelListView.as_view(), name='list'),
	path('create/', ChannelCreateView.as_view(), name='create'),
	path('<slug:slug>/', ChannelDetailView.as_view(), name='detail'),
]