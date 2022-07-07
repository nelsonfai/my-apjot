from django.contrib import admin

# Register your models here.
from .models import MediaUpload,Episodes,Podcomments

admin.site.register(MediaUpload)
admin.site.register(Episodes)
admin.site.register(Podcomments)