from django.forms import FileField, Form, ModelForm
from .models import userLogin


class ProductForm(ModelForm):
    class Meta:
        model = userLogin
        fields = ['studentname', 'batch', 'subject', 'credithour', 'grade', 'gradevalu', 'lcgpa', 'semlettergrade', 'remarks', 'dob', 'symb', 'result', 'subject1', 'credithour1', 'grade1', 'gradevalu1', 'semlettergrade1', 'remarks1', 'subject2', 'credithour2', 'grade2', 'gradevalu2', 'semlettergrade2', 'remarks2', 'subject3', 'credithour3', 'grade3', 'gradevalu3', 'semlettergrade3', 'remarks3']


class UploadForm(Form):
    products_file = FileField()