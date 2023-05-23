
from django import forms 
from .models import Comments

class CommentForm(forms.ModelForm):
    
    class Meta:
        model =Comments
        fields=['comment','name']

        widgets ={
            'name': forms.TextInput(attrs={'class':'name_field','placeholder':'Name','label':''}),
            'comment': forms.Textarea(attrs={'class': 'comment_field', 'placeholder': 'Enter comment here...', 'rows': 5}),

        }