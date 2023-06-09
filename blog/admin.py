from django.contrib import admin
from .models import Articles,Comments,Like,Contact,Category,NewsletterEmail,Highlights
# Register your models here.
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(NewsletterEmail)
admin.site.register(Highlights)

