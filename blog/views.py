from audioop import reverse

from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Articles, Like, Contact
from .forms import CommentForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy,reverse
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings


#Shared view data
def data():
    global articles_list
    articles_list=Articles.objects.all().order_by('-date')
    return articles_list



def bloghome(request):
       
       articles=data()
       related_articles=data()[1:5]
       p =Paginator(articles,per_page=2)
       page=request.GET.get('page')
       paginated_article=p.get_page(page)
       
       




    
       return render(request, 'blog/index.html',{'articles':related_articles,'paginated_article':paginated_article})

    
def article_details(request,courseid):
       articles= data()[1:5]
       article =Articles.objects.get(slug=courseid)
       single =Articles.objects.get(id=article.id)
       nextpost =Articles.objects.filter(id__gt=single.id).order_by('id').first()
       prevpost =Articles.objects.filter(id__lt=single.id).order_by('id').last()
       user= request.user
       comment_form = CommentForm()
       p=article.comments.all().order_by('-date')[0:5]

     
       
       
      
       pass_on ={
           'article':article,
           'comment_form':comment_form,
           'user':user,
           'prevpost':prevpost,
           'nextpost':nextpost,
           'articles':articles,
           'p':p
           
           
       }
       
       if request.method=='POST':

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                obj= comment_form.save(commit=False)
                obj.article = article
                obj.author = request.user
                obj.save()
                return redirect('details' ,courseid=article.slug)      
            else:
                comment_form =CommentForm()
           

       
       return render(request, 'blog/details.html',pass_on)

def search(request):
    
    if request.method == 'POST':
        searched =request.POST['search_input']
        k=Articles.objects.all()
        results = k.filter(body__contains=searched) 
        

        return render (request,'blog/search.html',{'searched':searched, 'results':results,})
      


def like_article(request,courseid):
    user=request.user
    if request.method=='POST':
        article_id=request.POST.get('article_id')
        article=Articles.objects.get(id=article_id)
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
        like, created =Like.objects.get_or_create(user=user,article_id=article_id)
        if not created:
            if like.value=='Like':
                like.value=='Unlike'
            else:
                like.value ='Like'
        like.save()




    return HttpResponseRedirect(reverse('details',args=[str(article.slug)]))
def contact(request):
    if request.method=="POST":
        contact=Contact() 
        name=request.POST.get('fname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        
        

        contact.name=name
        contact.subject=subject
        contact.email=email
        contact.message=message
        contact.time=datetime.now
        contact.save()
        # send email
        
        subject = f'Hi {name}Thank you for getting in touch' 
        message = f'Your message {message}  has been received. We will return to you as soon as possible'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail( subject, message, email_from, recipient_list )
        


    return HttpResponseRedirect(reverse('contact'))
