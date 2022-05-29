from django.db import models

# Create your models here.
#3 models location,category, image 

#1location
class Location(models.Model):
    location_name = models.CharField(max_length=45)
    def __str__(self):
        self.location_name
        
    def save_location(self):
        self.save
        
    def change_location(self):
        self.change_location
        
    def delete_location(self):
        self.delete_location
        
    
