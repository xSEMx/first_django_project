from django.urls import path
from django.contrib.auth.urls import urlpatterns as auth
from .views import *

urlpatterns = auth + [
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
]

