from django.shortcuts import render





def home(request):
    user =request.user
    return render(request, 'main/index.html' ,{'user':user})
def about(request):
    return render(request,'main/about.html')
def contact(request):
    return render(request,'main/contact.html')
