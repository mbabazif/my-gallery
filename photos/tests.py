from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.

class LocationTestClass(TestCase):
    '''
    test for Location class
    '''

    # Set up method
    def setUp(self):
        self.loc1= Location(country_name = 'Uganda', city_name ='Kampala')
  
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))

class CategoryTestClass(TestCase):
    '''
    test for Category class
    '''

    def setUp(self):
        self.new_cat= Category(category = 'travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_cat,Category))

class ImageTestClass(TestCase):
    '''
    test for Image class
    '''

    def setUp(self):
      
        self.loc1= Location(country_name = 'Uganda', city_name ='Kampala')
        self.loc1.save()

        
        self.new_cat = Category(category = 'travel')
        self.new_cat.save()

        self.new_image= Image(image = 'food1.jpeg',title = 'sky dive',description = 'a way to live adventure',category = self.new_cat,location = self.loc1)
        self.new_image.save()

        

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
            self.new_image.save()
            new_image = Image.objects.all()
            self.assertTrue(len(new_image) > 0)

    def test_get_all_images(self):
        images = Image.get_all()
        self.assertTrue(len(images)>0)
 

    def test_search_image(self):
        images = Image.search_image('pic')
        self.assertFalse(len(images)>0)