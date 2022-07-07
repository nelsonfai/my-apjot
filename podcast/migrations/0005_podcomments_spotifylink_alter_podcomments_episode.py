# Generated by Django 4.0.4 on 2022-07-07 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_rename_article_podlike_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcomments',
            name='spotifylink',
            field=models.CharField(default='1jQnF8PfdpYKo9Jguhinlc', max_length=200),
        ),
        migrations.AlterField(
            model_name='podcomments',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcomments', to='podcast.episodes'),
        ),
    ]
