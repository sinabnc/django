from django.shortcuts import render
from .models import Article,Service

# Create your views here.

def index(request):
    return render(request,"web/index.html")


def about(request):
    return render(request,"web/about.html")


def contact(request):
    return render(request,"web/contact-us.html")


def portfolio(request):
    return render(request,"web/portfolio.html")


def blog(request):
    articles = Article.objects.all()
    return render(request,"web/blog.html",{'articles': articles})


def service(request):
    services = Service.objects.all()
   
    return render(request,"web/services.html",{'services': services})