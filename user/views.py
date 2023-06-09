from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import CreateUserForm, Userloginform
from django.contrib import messages
from .models import CustomUser
from blog.models import NewsletterEmail

def login_view(request):
    if request.method=='POST':
        form = Userloginform(data=request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('../../blog')

    else:
        form = Userloginform()
    return render(request,'user/login.html',{'form':form})

    
def signup_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():  
            user = form.save()
            newletter = request.POST.get('myCheckbox')
            if newletter:
                print('Got the newsletter')
                try:
                    NewsletterEmail.objects.create(email=user.email)
                    print('Got the newsletter dONE')

                except:
                    print('Erotrr ')
                    pass

            login(request, user,backend='user.backends.EmailOrPhoneBackend')
            messages.success(request, 'Account successfully created')
            return redirect('../../blog')
    else:
        form = CreateUserForm()
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
        logout(request)
        return redirect('../../blog')
