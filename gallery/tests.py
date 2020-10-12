from django.test import TestCase
from .models import Photos, categories, Location

# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name = 'Ruiru')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoriesTestClass(TestCase):
    def setUp(self):
        self.category = categories(name='project')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, categories))

    def test_save_method(self):
        self.category.save_category()
        categories_object= categories.objects.all()
        self.assertTrue(len(categories_object)>0)


    

class PhotosTestClass(TestCase):
    def setUp(self):
        self.photo = Photos(image='imageurl', name='project', descripton='the intial step')

    def test_photo_instance(self):
        self.assertTrue(isinstance(self.photo, Photos))

    def test_save_photo_method(self):
        self.photo.save_image()
        photos = Photos.objects.all()
        self.assertTrue(len(photos)>0)