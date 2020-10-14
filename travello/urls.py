from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path("destinations", views.destinations, name ="destinations"),
    path("about", views.about, name ="about"),
    path("news", views.news, name ="news"),
    path("contact", views.contact, name ="contact"),
    path('search', views.search, name ='search')
]
