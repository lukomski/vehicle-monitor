from django import forms

class ImageUploadForm(forms.Form):
    f = forms.FileField()

class OccurenceForm(forms.Form):
    time = forms.DateTimeField()
    f = forms.FileField()