# Generated by Django 3.2.19 on 2023-06-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_articles_featured_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
