from django.test import TestCase
from .models import CarOccurence
from .views import *
from .plate_reader import PlateReader

class ViewsTests(TestCase):
    def test_index(self):
        self.assertTrue(True)
    
    def test_all_occurences(self):
        self.assertTrue(True)
        
    def car_occurence(self):
        self.assertTrue(True)

    def present_cars(self):
        self.assertTrue(True)
    
    def add_occurence(self):
        self.assertTrue(True)

    def plate_reader(self):
        self.assertTrue(True)


class ModelsTests(TestCase):
    def test_get_duration(self):
        self.assertTrue(True)


class PlateReaderTests(TestCase):
    def test_get_command(self):
        self.assertTrue(False)
    
    def test_read_license_plate(self):
        self.assertTrue(False)
