# Generated by Django 4.1.1 on 2022-11-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_post_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, default='yzzzzzzz', unique=True),
        ),
    ]
