"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

urlpatterns = [
    path('', PostList.as_view(), name = 'list'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', UserCreate.as_view(), name = 'register'),
    path('register-confirm/', register_confirm, name = 'register-confirm'),
    path('pass-reset/', PasswordResetView.as_view(), name = 'password_reset'),
    path('pass-reset-done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('pass-reset-confirm/<str:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('pass-reset-complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('<str:key>/', verify_activation_key, name = 'verify-user'),
]
