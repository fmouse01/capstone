from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Healthy

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'base.html', context)
    
    
def home(request):
    all_healthy = Healthy.objects.all()
    context = {
        'health': all_healthy
    }