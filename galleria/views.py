from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image

# Create your views here.
def pictures(request):
    images = Image.get_all_images()
    location = Location.objects.all()
    
    return render(request,'images.html',{'images':images,'locations':location})


#function for searching results
def search_results(request):
    categories = Category.objects.all()
    location = Location.objects.all()
    