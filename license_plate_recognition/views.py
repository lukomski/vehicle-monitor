from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.utils.timezone import utc
from django.db.models import Q

from .models import CarOccurence
from .plate_reader import PlateReader
from .forms import ImageUploadForm

import datetime

def index(request):
    return HttpResponse("SIEMA")

def all_occurences(request):
    occurences = CarOccurence.objects.all()
    
    return render(request, 'list.html', {'occurences': occurences})

def car_occurence(request, license_plate):
    occurences = get_list_or_404(CarOccurence, license_plate=license_plate)

    return render(request, 'list.html', {'occurences': occurences})


def present_cars(request):
    occurences = get_list_or_404(CarOccurence, dateof_exit__isnull=True)

    return render(request, 'list.html', {'occurences': occurences})

@csrf_exempt
def add_occurence(request):
    if request.method == 'POST':
        for key, value in request.FILES.items():
            plates = PlateReader.read_license_plate(value)
            for plate in plates:
                occurences = CarOccurence.objects.filter(license_plate=plate)
                started = occurences.filter(dateof_entry__isnull=False, dateof_exit__isnull=True)

                if occurences.count() == 0 or occurences.filter(Q(dateof_entry__isnull=True) | Q(dateof_exit__isnull=True)).count() == 0:
                    CarOccurence.objects.create(license_plate=plate, dateof_entry=datetime.datetime.utcnow().replace(tzinfo=utc))
                    continue
                
                if not started.first() is None:
                    occurence = started.first()
                    print(occurence)
                    occurence.dateof_exit = datetime.datetime.utcnow().replace(tzinfo=utc)
                    occurence.save()
                    continue
                
                print(type(occurences))


        return HttpResponse("POSZŁO")
    
    return HttpResponse("NO I NIC")

def plate_reader(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            license_plates = PlateReader.read_license_plate(request.FILES['f'])
            context = {
                'form': form,
                'plates': license_plates,
            }
            return render(request, 'upload.html', context)
        else:
            return HttpResponse('UPS')
    else:
        form = ImageUploadForm()
        return render(request, 'upload.html', {'form': form})