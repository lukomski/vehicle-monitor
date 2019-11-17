from django.core.files.uploadedfile import InMemoryUploadedFile
#from openalpr import Alpr
import subprocess

class PlateReader():

    @staticmethod
    def read_license_plate(image: InMemoryUploadedFile):
        # file to bytes
        image.read()
        ashCommand = "ls"
		
		#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		# output, error = process.communicate()
   #      alpr = Alpr("us")
   #      if not alpr.is_loaded():
   #        	print("Error loading OpenALPR")
   #        	return ['', '', 'Error loading OpenALPR']

   #      alpr.set_top_n(20)
 		# alpr.set_default_region("md")
   #      results = alpr.recognize_file("h786poj.jpg")

   #      i = 0
 		# for plate in results['results']:
   #   		i += 1
   #   		print("Plate #%d" % i)
   #   		print("   %12s %12s" % ("Plate", "Confidence"))
   #   		for candidate in plate['candidates']:
   #       		prefix = "-"
   #       		if candidate['matches_template']:
   #           		prefix = "*"

   #       		print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

 		# # Call when completely done to release memory
 		# alpr.unload()

        return ['1234', 'jeszcze jeden', 'EBE 12TC']