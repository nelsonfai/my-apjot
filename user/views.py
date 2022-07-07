from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CreateUserForm, Userloginform
from django.contrib import messages

def login_view(request):
    if request.method=='POST':
        form = Userloginform(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('../../blog')

    else:
        form = Userloginform()
    return render(request,'user/login.html',{'form':form})

    
def signup_view(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        
       
        if form.is_valid():
            user= form.save() 
            login(request,user)
            messages.success(request,'Account succesfully created')
            return redirect('../login')

    else:
        form= CreateUserForm()
    return render(request,'user/signup.html',{'form':form }) 

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('../../home')
