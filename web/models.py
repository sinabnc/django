from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField,PPOIField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(auto_now_add=True)
    meta_title = models.CharField(max_length=150)  # New field for meta title
    meta_description = models.TextField()  # New field for meta description
    alt_text = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
   

    def __str__(self):
        return self.name