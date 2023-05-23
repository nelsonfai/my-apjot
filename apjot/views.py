from django.shortcuts import render
from blog.models import Articles

def home(request):
    last_four_articles = Articles.objects.order_by('-id')[:3]
    user =request.user
    context= {
    'user':user,
    'articles':last_four_articles,
    'page_title':'Apjot: A public Journal of thoughts'
    }
    return render(request, 'main/index.html' ,context)
def about(request):
    context ={
            'page_title':'About us'
    }
    return render(request,'main/about.html',context)
def contact(request):
    context={
            'page_title':'Contact'
    }
    return render(request,'main/contact.html',context)
