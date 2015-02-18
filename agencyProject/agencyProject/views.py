from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect 

class agencyForm(forms.Form):
    
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")
    phone_number = forms.IntegerField(label = "Phone Number")
    
    
def home(request):
	return render(request, 'index.html', {})
    
def about(request):
    
    if request.method == 'POST':
        form = agencyForm(request.POST)
            
        if form.is_valid():
           agency = form()
           agency.first_name = form.cleaned_data["first name"]
           agency.last_name = form.cleaned_data["last name"]
           agency.email = form.cleaned_data["email"]
           agency.phone_number = form.cleaned_data["phone number"]
           agency.save()
           
           return HttpResponseRedirect('/thanks/')

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


