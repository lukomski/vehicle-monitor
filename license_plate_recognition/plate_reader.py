from django.core.files.uploadedfile import InMemoryUploadedFile
import subprocess
import re

class PlateReader():

    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        # file to bytes
        image.read()
        file_name = "samochod.jpg" # h786poj.jpg
        # save image to file TODO - now use static file

        # use aplr to read licence plate
        bashCommand = "alpr /code/" + file_name
		
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
        
        m = re.search('-\s*(.*)\s*\\t\s*confidence', output.decode('utf-8'))
        plate_text = m.group(1)

        return ['1234', 'jeszcze jeden', plate_text]