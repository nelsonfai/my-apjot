from django.shortcuts import render
from blog.models import Articles
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    last_four_articles = Articles.objects.filter(publish=True).order_by('featured_order')[:3]
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




class MySitemap(Sitemap):
   def location(self, obj):
    # For dynamic objects
    if isinstance(obj, Articles):
        return reverse('details', args=[obj.slug])
    # For static pages
    elif obj == '':
        return ''
    elif obj == 'blog':
        return '/blog/'
    elif obj == 'about':
        return '/about/'
    
   def items(self):
        return [ '','blog', 'about'] + list(Articles.objects.all())


sitemaps = {
    'my_sitemap': MySitemap,
}
def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")
