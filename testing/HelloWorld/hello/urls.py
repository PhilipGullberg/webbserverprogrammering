from django.urls import path
from django.urls import include
from . import views

urlpatterns=[
    path('',views.cool, name="cool" ),
    path('task/', views.add, name="add"),
    path('home/',views.cool, name="cool" ),
    path('about/', views.about, name="cool" ),
    path('philip/',views.hello, name="hello" ),

]
