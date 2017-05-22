from django.shortcuts import render
from django.contrib import admin
from . import views

# Create your views here.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
        url(r'^$', views.index),
]
from django.contrib import admin
    url(r'^$', views.index)
