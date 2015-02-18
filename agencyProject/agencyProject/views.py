from django.shortcuts import render
from django.http import HttpResponseRedirect
from agencyProject import models
from agencyProject.forms import agencyForm, share_form


def home(request):
    return render(request, 'index.html', {})
    
def about(request):
    
    if request.method == 'POST':
        form = agencyForm(request.POST)
            
        if form.is_valid():
           agency = models.form()
           agency.first_name = form.cleaned_data["first_name"]
           agency.last_name = form.cleaned_data["last_name"]
           agency.email = form.cleaned_data["email"]
           agency.phone_number = form.cleaned_data["phone_number"]
           agency.save()
           
           return HttpResponseRedirect('/')

    else:
        form = agencyForm()
        
        
    return render(request, 'about.html', {'form': form})

        #return HttpResponseRedirect("/404/")
    
    #return render(request, 'about.html', {})

def campaigns(request):
    return render(request, 'campaigns.html', {})

def campaigns_pages(request):
    return render(request, 'campaigns_pages.html', {})

def splash(request):
    return render(request, 'splash.html', {})

def share(request):
    if request.method == 'POST':
        form = share_form(request.POST)

        if form.is_valid():
            share = models.share_form
            share.first_name = form.cleaned_data["first name"]
            share.last_name = form.cleaned_data["last name"]
            share.receiver_email = form.cleaned_data["receiver_email"]
            share.sender_email = form.cleaned_data["sender_email"]
            share.receiver_phone = form.cleaned_data["receiver_phone"]
            share.sender_phone = form.cleaned_data["sender_phone"]
            share.save()

            return HttpResponseRedirect('/')

    else:
        form = share_form()

    return render(request, 'share.html', {'form': form})

    return render(request, 'share.html', {})