from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class LocationTestCase(TestCase):
    def setUp(self):
        self.location = Location(location_name='kamakis')
    
    def tearDown(self):
        Location.objects.all().delete()
        
        
    #test the instance
    def test_instance(self):
        self.assertTrue(self.location,Location)
        
    
    
class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category(category_name='Business')
        
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))




class ImageTestCase(TestCase):
    def setUp(self):
        self.location = Location(location_name= 'kamakis')
        self.location.save()
        
        self.category = Category(category_name='Tourism')
        self.category.save()
        
        self.image_test = Image(image_name='image_test',image_description='Testing the image',category=self.category,location=self.location)
        
    def test_instance(self):
        self.AssertTrue(isinstance.self.image_test,Image)
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
        
        
        
    
        
    
        
    
