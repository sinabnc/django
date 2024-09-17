from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField,PPOIField
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = HTMLField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(auto_now_add=True)
    meta_title = models.CharField(max_length=150)  # New field for meta title
    meta_description = models.TextField()  # New field for meta description
    alt_text = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse_lazy("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('date',)
        verbose_name = ('Blog')
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title
# Create your models here.




    

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def get_absolute_url(self):
        return reverse_lazy("service_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = ('Service')
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name