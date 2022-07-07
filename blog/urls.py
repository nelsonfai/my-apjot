
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.bloghome, name="blogHome"),
    path('<slug:courseid>', views.article_details, name="details"),
    path('search/',views.search, name='search'),
    path('<slug:courseid>/like',views.like_article, name='like_article'),
    path('contactprocess/',views.contact, name='contactprocess'),
   
    
]