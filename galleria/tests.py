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
        
    def test_save_location(self):
        self.location.save_location()
        locations= Location.objects.all()
        self.assertFalse(len(locations)>0)
        #updating location test
    def test_update_location(self):
        #self.location.update_location()
        #updated_location= Location.objects.filter(location=locations)
        new_location_name = 'Nanyuki'
        self.location.update_location(self.location.id,new_location_name)
        updated_location= Location.objects.filter(location_name='Nanyuki')
        self.assertFalse(len(updated_location)>0)
        
    def test_delete_location(self):
        self.location.delete_location()
        location= Location.objects.all()
        self.assertTrue(len(location)==0)
        
    
    
class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category(category_name='Business')
        
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
        
        #test save() method
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertFalse(len(categories)>0)
        
    def test_update_category(self):
        self.category.update_category()
        updated_category= Category.objects.filter(category_name='Travel')
        self.assertFalse(len(updated_category)>0)
        
        
    def test_delete_category(self):
        self.category.delete_category()
        category= Category.objects.all()
        self.assertTrue(len(category)==0)
        




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
        
        
        
        
    
        
    
        
    
