# Generated by Django 4.0.4 on 2022-11-30 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comments_author_comments_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(default='', max_length=222),
        ),
        migrations.CreateModel(
            name='Applaud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applaudCount', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applaud', to='blog.articles')),
            ],
        ),
    ]
