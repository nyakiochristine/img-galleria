from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image

# Create your views here.
#function for searching results
def search_results(request):
    categories = Category.objects.all()
    location = Location.objects.all()
    