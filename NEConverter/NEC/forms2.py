from django import forms
from .models import Imageo

class ImageForm(forms.ModelForm):
    class Meta:
        model = Imageo
        fields = ('file',)