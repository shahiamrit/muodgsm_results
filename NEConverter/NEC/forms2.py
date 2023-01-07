from django import forms
from .models import Imageo
from PIL import Image
from django.core.files import File

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Imageo
#         fields = ('file',)



# working code
class ImageForm(forms.ModelForm):
    class Meta:
        model = Imageo
        fields = ('file',)

    def save(self):
        photo = super(ImageForm, self).save()
        image = Image.open(photo.file)
        resized_image = image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
# working code