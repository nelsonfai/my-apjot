# Generated by Django 3.2.19 on 2023-05-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_articles_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='featured_order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
