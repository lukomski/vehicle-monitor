from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('plate_reader', views.plate_reader, name='plate_reader'),
    path('all', views.all_occurences, name='all'),
    path('present', views.present_cars, name='present_cars'),
    path('<str:license_plate>/details', views.car_occurence, name='car_occurence'),
    path('new', views.add_occurence, name='add_occurence')
]