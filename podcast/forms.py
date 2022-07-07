
from django import forms 
from .models import Podcomments

class CommentForm(forms.ModelForm):
    
    class Meta:
        model =Podcomments
        fields=['comment']

        widgets ={
            'name': forms.TextInput(attrs={'class':'name_field','placeholder':'Name','label':''}),
            'comment': forms.Textarea(attrs={'class':'comment_field','placeholder':'Leave a comment...','rows':54})
        }