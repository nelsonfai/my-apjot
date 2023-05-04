from django.contrib import admin
from .models import Articles,Comments,Like,Contact,Category
# Register your models here.
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Contact)
admin.site.register(Category)

