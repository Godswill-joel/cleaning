from django.shortcuts import render
from project.models import Services,Post
# Create your views here.

def index (request):
    context = {}
    return render(request, 'index.html', context)

def about (request):
    context = {}
    return render(request, 'about.html', context)

def contact (request):
    context = {}
    return render(request, 'contact.html', context)

def project (request):
    context = {}
    return render(request, 'project.html', context)

def service (request): 
    context = {
        'project' : Services.objects.all()
    }
    return render(request, 'service.html', context)

def blog (request):
    context = {
        'project': Post.objects.all()
    }
    return render(request, 'blog.html', context)

def choose (request):
    context = {}
    return render(request, 'choose.html', context)
