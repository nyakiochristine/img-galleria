from django.urls import path
from . import views


urlpatterns = [
    path('',views.galleria,name='galleria')
    
]


