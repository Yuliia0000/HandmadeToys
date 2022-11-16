from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def info(request):
    return render(request, 'home/info.html')

def contact(request):
    return render(request, 'home/contact.html')
