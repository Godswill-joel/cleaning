from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def portfolio (request):
    return render(request, 'portfolio.html')

def service (request):
    return render(request, 'service.html')

