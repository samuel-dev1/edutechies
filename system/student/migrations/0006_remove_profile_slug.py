# Generated by Django 4.1.1 on 2022-11-14 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
