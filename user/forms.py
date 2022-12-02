
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']
        
        widgets ={
            'username': forms.TextInput(attrs={'class':'field','placeholder':'Name',}),
            'email': forms.TextInput(attrs={'class':'field','placeholder':'Email',}),
            'password1': forms.PasswordInput(attrs={'class':'field','placeholder':'Name',}),
            'password2': forms.PasswordInput(attrs={  'class':'field','placeholder':'Name',})
        }

        
class Userloginform(AuthenticationForm):
    class Meta:
        model=User
        fields =['username','password']
    
        widgets ={

            'username': forms.TextInput(attrs={'class':'field','placeholder':'username',}),
            'password':forms.PasswordInput(attrs={'class':'field','placeholder':'password',}),
            
        }