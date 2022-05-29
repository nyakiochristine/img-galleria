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
        
    
#2 category class   
class Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        self.category_name
        
    def save_category(self):
        self.save
        
    
    def change_category(self):
        self.change_category
        
    def delete_category(self):
        self.delete_category
        
class Image(models.Model):
    image_name = models.CharField(max_length=25)
    image_description = models.TextField(max_length=75)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
    
