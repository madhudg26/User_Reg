from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse



def home(request):
    return render(request,'home.html')



def registrations(request):
    uf=UserForm()
    pf=PeofileForm()
    d={'uf':uf,'pf':pf}

    if request.method=="POST" and request.FILES:
        UFD=UserForm(request.POST)
        PFD=PeofileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            UFO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            UFO.set_password(password)
            UFO.save()

            PFO=PFD.save(commit=False)
            PFO.profile_user=UFO
            PFO.save()
            return HttpResponse('registration is successfull')
        
    return render(request,'registrations.html',d)
