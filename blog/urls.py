from django.urls import path
from .views import (
		PostList,
		PostDetail,
		PostCreate,
		PostUpdate,
		PostDelete,
	) 

app_name = 'blog'

urlpatterns = [
	path('', PostList.as_view(), name = 'list'),
	path('<int:pk>/', PostDetail.as_view(), name = 'detail'),
	path('create/', PostCreate.as_view(), name = 'create'),
	path('update/<int:pk>/', PostUpdate.as_view(), name = 'update'),
	path('delete/<int:pk>/', PostDelete.as_view(), name = 'delete'),
]