from django.shortcuts import render
from django.views.generic import ListView



def homepageview(request):
    return render(request,'home.html')

