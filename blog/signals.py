from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Articles
import requests
print('IN barca')
@receiver(post_save, sender=Articles)
def article_created(sender, instance, created, **kwargs):
    if created:
        # Perform actions or logic when a new article is created
        # For example:
        print("New article created:", instance.title)
        # You can include any additional actions you need here
        if instance.post_medium:
            title = instance.title
            content = instance.body
            tags = list(instance.tags.names())  # Convert queryset to list
            access_token = "2acb799cb1df1634463cf85d113ffaae9ec28e299eb20ad5675f34f7109f2abf5"
            response = publish_to_medium(title, content, tags, access_token)
            print(response)

def publish_to_medium(title, content, tags, access_token):
    url = "https://api.medium.com/v1/users/self/posts"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "tags": tags,
        "publishStatus": "draft",
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    return response.json()