# Generated by Django 4.0.4 on 2022-12-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_articles_applaud_articles_views_delete_applaud'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
