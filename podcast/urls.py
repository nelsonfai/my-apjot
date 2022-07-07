
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.podcasthome ,name='podcastHome'),
    path('<slug:slug>', views.episodes, name='episode'),
    path('search/',views.podcastsearch, name='podcastsearch'),
    path('<slug:slug>/like',views.like_podcast, name='like_podcast'),
   
]