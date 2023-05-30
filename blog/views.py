from audioop import reverse
from django.db import IntegrityError
from django.db.utils import IntegrityError as DjangoIntegrityError

from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Articles, Like, Contact
from .forms import CommentForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy,reverse
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import  JsonResponse
from .models import NewsletterEmail

#Shared view data
def data():
    global articles_list
    articles_list=Articles.objects.filter(publish=True).order_by('-date')
    return articles_list

def bloghome(request):
       category= request.GET.get('category')
       categories = {
    'plr': 'Philosophy and life reflections',
    'pdg': 'Personal development and growth',
    'scc': 'Social and Cultural commentary',
    'ins': 'Inspirational stories',
    'mwb': 'Mindfulness and Well being'
}
       active = 'All'
       if category:
            if category == 'All':
                articles=data()
            else:
                articles = Articles.objects.filter(publish=True).filter(category=category).order_by('-date')
                active = category
       else:
            articles=data()  
       p=Paginator(( articles ),per_page=8)
       page=request.GET.get('page')
       paginated_article=p.get_page(page)
       return render(request, 'blog/index.html',{'paginated_article':paginated_article,'category':categories,'active':active,'page_title':'Blogs : Apjot'
})

def article_details(request,courseid):
        article =Articles.objects.get(slug=courseid)
        if request.method=='POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                obj= comment_form.save(commit=False)
                obj.article = article
                obj.save()
             #   return redirect('details' ,courseid=article.slug)      
            #else:
             #   comment_form =CommentForm()
                return JsonResponse({'name': obj.name, 'comment': obj.comment ,'status':'form submitted'})
            else:
                return JsonResponse({'status':'form not submitted'})
        else:
                articles= data()[1:5]
                article.views +=1
                article.save()
                single = Articles.objects.get(id=article.id)
                nextpost =Articles.objects.filter(publish=True).filter(id__gt=single.id).order_by('id').first()
                prevpost =Articles.objects.filter(publish=True).filter(id__lt=single.id).order_by('id').last()
                user= request.user
                comment_form = CommentForm()
                p=article.comments.all().order_by('date')[0:10]
                pass_on ={
                    'article':article,
                    'comment_form':comment_form,
                    'user':user,
                    'prevpost':prevpost,
                    'nextpost':nextpost,
                    'articles':articles,
                    'p':p ,
                    'page_title':f'Apjot: {article.title}'
 
                }
        return render(request, 'blog/details.html',pass_on)
def search(request):
        searched =request.GET['searchterm']
        if searched:
            k=Articles.objects.filter(body__contains=searched) 
            p=Paginator((k ),per_page=5)
            page=request.GET.get('page')
            paginated_article=p.get_page(page)
            count = k.count
        else:
             results = ''
             count = 0
        return render(request, 'blog/index.html',{'paginated_article':paginated_article,'searched':searched,'count':count})
      
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

def applaud(request,courseid):
    if request.method=='POST':
        article_id=request.POST.get('article_id')
        article=Articles.objects.get(id=article_id)
        article.applaud += 1
        article.save()
        return JsonResponse({'applaudcount': article.applaud})
    else:
        return JsonResponse({'applaudcount': article.applaud})
   
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


def subscribe(request):
    if request.method == 'POST':
                email = request.POST.get('email')
                if email:
                    if NewsletterEmail.objects.filter(email=email).exists():
                        return JsonResponse({'message': 'You are already registered to Newsletter'})
                    else:
                        NewsletterEmail.objects.create(email=email)
                        return JsonResponse({'message': 'Email added  successfully!'})


    return JsonResponse({'error':'Opps something went wrong .Please try again!'})

