# Generated by Django 3.2.18 on 2023-05-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230504_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='password_required',
            field=models.BooleanField(default=False),
        ),
    ]