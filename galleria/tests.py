from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        self.location = Location(location_name= 'kamakis')
        self.location.save()
        
        self.category = Category(category_name='Tourism')
        self.category.save()
        
        self.image_test = Image(image_name='image_test',image_description='Testing the image',category=self.category,location=self.location)
        
    
        
    
