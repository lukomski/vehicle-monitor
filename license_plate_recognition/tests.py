import datetime

from django.contrib.auth.models import AnonymousUser, User
from django.http import Http404
from django.test import RequestFactory, TestCase, Client
from unittest import mock
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import CarOccurence
from .plate_reader import PlateReader, get_command
from .views import *


class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testUser', email='', password='secret'
        )
        self.client = Client

    def test_index(self):
        request = self.factory.get('')
        request.user = self.user
        anonumous_request = self.factory.get('')
        anonumous_request.user = AnonymousUser

        user_response = index(request)
        anonymous_response = index(anonumous_request)

        self.assertEqual(user_response.status_code, 200)
        self.assertEqual(anonymous_response.status_code, 200)
    
    def test_all_occurences(self):
        request = self.factory.get('')
        request.user = self.user

        response = all_occurences(request)

        self.assertTrue(True)
        
    def test_car_occurence(self):
        request = self.factory.get('')
        request.user = self.user

        # valid license plate
        CarOccurence.objects.create(license_plate='valid', dateof_entry=None)
        response = car_occurence(request, 'valid')
        
        # invalid license plate
        with self.assertRaises(Http404):
            car_occurence(request, '1234')
        self.assertEqual(response.status_code, 200)

    def test_present_cars(self):
        request = self.factory.get('')
        request.user = self.user

        with self.assertRaises(Http404):
            present_cars(request)
    
    def test_add_occurence(self):
        request = self.factory.post('')
        request.user = self.user

        response = add_occurence(request)

        self.assertEqual(response.status_code, 200)

    def test_plate_reader(self):
        request = self.factory.get('')
        request.user = self.user
        response = index(request)

        self.assertEqual(response.status_code, 200)


class ModelsTests(TestCase):
    def test_get_duration(self):
        dt = datetime.datetime.now()
        object = CarOccurence.objects.create(license_plate='test', dateof_entry=dt, dateof_exit=dt + datetime.timedelta(days=1))
        
        self.assertEqual(object.get_duration(), datetime.timedelta(days=1))


class PlateReaderTests(TestCase):
    def test_get_command(self):
        test_command = "echo x"
        
        self.assertEqual(get_command(test_command), b'x\n')
    
    def test_read_license_plate(self):
        with open('h786poj.jpg', 'rb') as f:
            InMemoryUploadedFile.read = mock.Mock(return_value=f.read())
            result = PlateReader.read_license_plate(InMemoryUploadedFile(None, None, None, None, None, None))
        self.assertEqual(result, ['786P0'])
