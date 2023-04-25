from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monitoring_vus/', include('monitoring_vus.urls')),
    path('account/', include('accounts.urls')),
]
