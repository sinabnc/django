from django.shortcuts import render
from .models import Blog,Service

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
    blogs = Blog.objects.all()
    context = {"is_blog": True,
               "blogs": blogs}
    return render(request, "web/blog.html", context)

def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    other_blogs = Blog.objects.all().exclude(slug=slug)
    context = {"is_blog": True,
               "blog": blog,
               "other_blogs": other_blogs}
    
    return render(request, "web/blog-single.html", context)



def service(request):
    services = Service.objects.all()
    context = {"is_service": True,
               "services": services
               }
    return render(request, "web/services.html", context)

def service_detail(request,slug):
    service = Service.objects.get(slug=slug)
    other_services = Service.objects.all().exclude(slug=slug)
    context = {"is_service": True,
               "service": service,
               "other_services": other_services,
               }
    return render(request, "web/service-single.html", context)
