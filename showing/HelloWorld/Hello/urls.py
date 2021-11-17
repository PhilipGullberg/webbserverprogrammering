from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('add/', views.add, name="add"),

]