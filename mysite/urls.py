from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
                                    LoginView, 
                                    LogoutView,
                                    PasswordResetView,
                                    PasswordResetDoneView,
                                    PasswordResetConfirmView,
                                    PasswordResetCompleteView,
                                )
from blog.views import PostList
from profiles.views import UserCreate, register_confirm, verify_activation_key
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('auth/', include('social_django.urls')),
    path('u/', include('profiles.urls')),
    path('c/', include('channel.urls')),
    path('', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', UserCreate.as_view(), name = 'register'),
    path('register-confirm/', register_confirm, name = 'register-confirm'),
    path('pass-reset/', PasswordResetView.as_view(), name = 'password_reset'),
    path('pass-reset-done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('pass-reset-confirm/<str:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('pass-reset-complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('activate/<str:key>/', verify_activation_key, name = 'verify-user'),
]
