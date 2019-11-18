from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import subprocess
import re

class PlateReader():

    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        # file to bytes
        image.read()
        file_name = "samochod.jpg" # h786poj.jpg
        # save image to file TODO - now use static file
        path = default_storage.save('file.jpg', ContentFile(image.read()))
        #print("path = " + path)


        # use aplr to read licence plate
        bashCommand = "alpr /code/" + file_name
        #bashCommand = "alpr /code/" + path
        #print("bashCommand = " + bashCommand)

		
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        m = re.search('-\s*(.*)\s*\\t\s*confidence', output.decode('utf-8'))
        plate_text = m.group(1)

        return ['1234', 'jeszcze jeden', plate_text]