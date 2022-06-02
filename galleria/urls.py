from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('',views.pictures, name='pictures'),
    path('search/', views.search_results, name='search_results'),
    path('location/(<location_name>\)/', views.get_image_by_location, name='location'),
    

]


#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)