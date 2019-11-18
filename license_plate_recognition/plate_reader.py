from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import subprocess
import re

class PlateReader():

    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        file_name = 'samochod.jpg'
        with open(file_name, 'wb') as f:
            f.write(image.read())

        bashCommand = "alpr /code/" + file_name
		
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        m = re.search('-\s*(.*)\s*\\t\s*confidence', output.decode('utf-8'))
        print(output.decode('utf-8'))
        plate_text = m.group(1)

        return ['1234', 'jeszcze jeden', plate_text]