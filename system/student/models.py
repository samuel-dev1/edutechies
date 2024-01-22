from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import random, string




# Create your models her

class Profile(models.Model):
    choice = (("web development", "web developmnet"), ("app development", "app develpment"), ("web design", 'web design'), ("others", "others"))
    system_ram = models.IntegerField(default=2)
    phone_number = models.CharField(max_length=11)
    club_department =models.CharField(choices=choice, max_length=100)
    department = models.CharField(max_length=200)
    card_picture =models.ImageField(upload_to="idcard", default='default.png')
    user = models.OneToOneField(User, on_delete =models.CASCADE,related_name ="user_account")
    slug = models.SlugField(blank=True)
    
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        global t
        t = "".join(random.choice(string.ascii_lowercase+string.digits) for x in range(11))
        t_to_str = str(t)
        Profile.objects.create(user =instance, slug = t_to_str, department = "educational Technology")
                
class Post(models.Model):
    picture =models.ImageField(upload_to="admins")
    twittter = models.CharField(max_length=300)
    whatsapp =models.CharField(max_length=200)
    name =models.CharField(max_length=200)
    experties_area =models.CharField(max_length=200)
    
    
class Assingment(models.Model):
    assignment = models.CharField(max_length=400)
    
class icon(models.Model):
    icon =models.ImageField(upload_to="icons")
    
    
    
    
    