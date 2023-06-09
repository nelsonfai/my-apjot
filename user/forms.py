from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from user.models import CustomUser
from django.contrib.auth import authenticate

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')

    class Meta:
        model = CustomUser
        fields = ['email', 'password1']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Password'}),
        }
    def cleaned_data(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")

class Userloginform(forms.Form):
    email = forms.CharField( max_length=255, widget=forms.TextInput(attrs={'placeholder': ' Email address'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
         # authenticate user
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Invalid login credentials.Keep in my password is case sensitive')
        self.user = user
        return self.cleaned_data