
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Articles (models.Model):
    title = models.CharField( max_length=100)
    #body = models.TextField()
    body = RichTextField( blank=True, null=True)
    slug = models.SlugField()
    date =models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    likes =models.ManyToManyField(User, default=None,blank=True, related_name='liked')
    tagline=models.CharField(max_length=100 ,blank=True,default=True)
    views = models.IntegerField(default=0)
    applaud = models.IntegerField(default=0)
    publish=models.BooleanField(default=False)

    def __str__(self):
        return self.title +' | ' + str (self.date)

    def snippet(self):
        return self.body[:240] + "..."  
    
    @property
    def num_likes(self):
        return self.liked.all().count()

class Comments (models.Model):
    name = models.CharField(max_length=222 ,default='')
    article= models.ForeignKey(Articles, related_name='comments' ,on_delete= models.CASCADE)
    comment= models.TextField()
    date= models.DateTimeField(auto_now=True)
    
    author =models.ForeignKey(User,on_delete= models.CASCADE,default=1) 
    

    def __str__(self):
        return f'{self.author.id} commented on {self.article.title}' 
    
LIKE_CHOICES=(
    ('Like','Like'), ('Unlike','Unlike'))

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Articles,on_delete=models.CASCADE)
    value =models.CharField(choices =LIKE_CHOICES, default='Like', max_length=10)
   





class Contact(models.Model):
    name=models.CharField(max_length=100)
    email= models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
   
    
    def __str__(self):
        
        return   self.subject +  '  from: '+ '[ '+ self.name +']'+ 'at'  + self.time.strftime("%a, %d %b %Y  %H{+2}:%M ")
