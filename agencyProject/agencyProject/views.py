from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'index.html', {})
    
def about(request):
	return render(request, 'about.html', {})

def campaigns(request):
	return render(request, 'campaigns.html', {})

def campaigns_pages(request):
	return render(request, 'campaigns_pages.html', {})

def splash(request):
	return render(request, 'splash.html', {})


