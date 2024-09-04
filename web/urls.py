from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.index,name="index"), 
    path("about/",views.about,name="about"), 
    path("contact/",views.contact,name="contact"), 
    path("portfolio/",views.portfolio,name="portfolio"), 
    path("blog/",views.blog,name="blog"), 
    path("service/",views.service,name="service"), 



]