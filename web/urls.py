from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.index,name="index"), 
    path("about/",views.about,name="about"), 
    path("contact/",views.contact,name="contact"), 
    path("portfolio/",views.portfolio,name="portfolio"), 
    path("blog/",views.blog,name="blog"), 
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("service/",views.service,name="service"), 
    path("service_detail/<slug:slug>/",views.service_detail,name="service_detail"), 




]