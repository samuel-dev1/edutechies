# Generated by Django 4.1.1 on 2022-11-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
