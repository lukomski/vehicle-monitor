from django.core.files.uploadedfile import InMemoryUploadedFile
class PlateReader():

    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        # file to bytes
        image.read()
        
        return ['1234', 'jeszcze jeden', 'EBE 12TC']