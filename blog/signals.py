'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Articles
import requests


print('IN barca')
@receiver(post_save, sender=Articles)
def article_created(sender, instance, created, **kwargs):
    if created:
        print("New article created:", instance.title)
        if instance.post_medium:
            title = instance.title
            content = instance.body
            tags = list(instance.tags.names())
            author_id = "1119602260574705623"  # Replace with the actual authorId
            access_token = "2acb799cb1df1634463cf85d113ffaae9ec28e299eb20ad5675f34f7109f2abf5"
            response = publish_to_medium(title, content, tags, author_id, access_token)
            print(response)

def publish_to_medium(title, content, tags, author_id, access_token):
    url = f"https://api.medium.com/v1/users/{author_id}/posts"
    headers = {
        'Host': 'api.medium.com',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "tags": tags,
        "publishStatus": "draft"
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        response.raise_for_status()
        print("Article published successfully:", response.json())
    except requests.exceptions.HTTPError as error:
        print("Error publishing article:", error)
        print("Response content:", response.content)

    return response.json()

'''