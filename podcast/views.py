from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Episodes, PodLike
from .forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def data():
    episodes=Episodes.objects.all().order_by('-date')
    return episodes



def podcasthome(request):
    episodes=Episodes.objects.all().order_by('-date')[1:]
    first_episode=Episodes.objects.all().order_by('-date').first()
    context={
        'episodes':episodes,
        'first_episode':first_episode
    }


    return render(request,'podcast/index.html' ,context)
 
def episodes(request,slug):
       episodes= data()
       episode =Episodes.objects.get(slug=slug)
       single =Episodes.objects.get(id=episode.id)
       nextpost =Episodes.objects.filter(id__gt=single.id).order_by('id').first()
       prevpost =Episodes.objects.filter(id__lt=single.id).order_by('id').last()
       user= request.user
       comment_form = CommentForm()
       comments=episode.podcomments.all().order_by('-date')[0:5]
       

           
       
      
       pass_on ={
           'episode':episode,
           'comment_form':comment_form,
           'user':user,
           'prevpost':prevpost,
           'nextpost':nextpost,
           'episodes':episodes,
           'comments':comments
           
           
       }
       
       if request.method=='POST':

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                obj= comment_form.save(commit=False)
                obj.episode = episode
                obj.author = request.user
                obj.save()
                return redirect('episode' ,slug=episode.slug)      
            else:
                comment_form =CommentForm()
           

       
       return render(request, 'podcast/episode.html',pass_on)


    

def podcastsearch(request):
    
    if request.method == 'POST':
        searched =request.POST['search_input']
        k=Episodes.objects.all()
        results = k.filter(title__contains=searched)    
        return render (request,'podcast/search.html',{'searched':searched, 'results':results,})


def like_podcast(request,slug):
    user=request.user
    if request.method=='POST':
        episode_id=request.POST.get('episode_id')
        episode=Episodes.objects.get(id=episode_id)
        if user in episode.likes.all():
            episode.likes.remove(user)
        else:
            episode.likes.add(user)
        like, created =PodLike.objects.get_or_create(user=user,episode_id=episode_id)
        if not created:
            if like.value=='Like':
                like.value=='Unlike'
            else:
                like.value ='Like'
        like.save()




    return HttpResponseRedirect(reverse('episode',args=[str(episode.slug)]))   