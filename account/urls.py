# account/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='my_logout'),
    path('register/', views.register, name='register'),  
    path('profile/', views.profile.as_view(), name='profile'),  
]
