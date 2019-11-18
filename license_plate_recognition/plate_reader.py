from django.core.files.uploadedfile import InMemoryUploadedFile
import subprocess
import re

def get_command(command):		
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output

class PlateReader():
    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        file_name = 'samochod.jpg'
        with open(file_name, 'wb') as f:
            f.write(image.read())
        
        output = get_command(f"alpr /code/{file_name}")

        m = re.search('-\s*(.*)\s*\\t\s*confidence', output.decode('utf-8'))
        print(output.decode('utf-8'))
        plate_text = m.group(1)

        return [plate_text]