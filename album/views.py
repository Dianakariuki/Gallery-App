from django.shortcuts import render
from .models import Image, Category, Location
from django.http import HttpResponse, Http404

def welcome(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'categories.html',{"categories":categories,"locations":locations})

