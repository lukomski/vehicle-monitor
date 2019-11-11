from django.db import models

class CarOccurence(models.Model):
    license_plate = models.CharField(max_length=50)
    dateof_entry = models.DateTimeField(null=True, blank=True)
    dateof_exit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.license_plate

    def get_duration(self):
        return self.dateof_exit - self.dateof_entry