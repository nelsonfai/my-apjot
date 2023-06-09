from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from user.models import CustomUser


# Create your models here.
class MediaUpload(models.Model):
    name= models.CharField(max_length=100)
    image=models.FileField()
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Episodes(models.Model):
    title = models.CharField( max_length=100)
    #duration =models.
    description = RichTextField( blank=True, null=True)
    slug = models.SlugField()
    date =models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    likes =models.ManyToManyField(CustomUser, default=None,blank=True, related_name='podliked')
    spotifylink=models.CharField(max_length=200 ,default='1jQnF8PfdpYKo9Jguhinlc')
    
    def __str__(self):
        return self.title +' | ' + str (self.date)

    def snippet(self):
        return self.description[:100] + "..."  
    @property
    def num_likes(self):
        return self.liked.all().count()

class Podcomments (models.Model):
    episode= models.ForeignKey(Episodes, related_name='podcomments' ,on_delete= models.CASCADE)
    comment= models.TextField()
    date= models.DateTimeField(auto_now=True)
    author=models.ForeignKey(CustomUser, related_name='podcomment_author' ,on_delete= models.CASCADE,default=1)
   
    def __str__(self):
        return f'{self.author.username} commented on {self.episode.title}' 



    
LIKE_CHOICES=(
    ('Like','Like'), ('Unlike','Unlike'))

class PodLike(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    episode=models.ForeignKey(Episodes,on_delete=models.CASCADE)
    value =models.CharField(choices =LIKE_CHOICES, default='Like', max_length=10)
    
   
