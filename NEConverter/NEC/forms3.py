from django.forms import FileField, Form, ModelForm
from .models import userLogin


class ProductForm(ModelForm):
    class Meta:
        model = userLogin
        fields = ['id', 'name', 'instuation', 'position', 'phone', 'email', 'emisurl', 'username', 'password', 'scode']


class UploadForm(Form):
    products_file = FileField()