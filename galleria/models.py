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
        
    def update_location(self):
        self.update_location
        
    @classmethod
    def update_location(cls, id,value):
            cls.objects.filter(id=id,value=value).update(location_name=value)
        
    def delete_location(self):
        self.delete_location
        
    
#2 category class   
class Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        self.category_name
        
    def save_category(self):
        self.save
        
    
    def update_category(self):
        self.update_category
        
        
    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id=id,value=value).update(category_name=value)
        
        
    def delete_category(self):
        self.delete_category
        
class Image(models.Model):
    image_name = models.CharField(max_length=25)
    image_description = models.TextField(max_length=75)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'pictures')
    
    def __str__(self):
        return self.image_name
    
    
    def save_image(self):
        self.save
        
        
    def delete_image(self):
        self.delete_image
        
    class Meta:
        ordering = ['image_name']   
        
    @classmethod
    def get_all_images(cls):
        images =cls.objects.all()
        return images
    
    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id,value=value).update(image=value)
        
        
    @classmethod
    def get_image_by_id(cls,search_term):
        image = cls.objects.filter(image_id=search_term)
        return image
    
    @classmethod
    def filter_by_location(cls,search_term):
        locations = cls.objects.filter(location__location_name__icontains=search_term)
        return locations
    
    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__)
    
