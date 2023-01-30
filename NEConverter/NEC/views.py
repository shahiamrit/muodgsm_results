from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from pyBSDate import convert_BS_to_AD
# from .forms import UserInputForms
# from .forms2 import ImageForm
from django.http import JsonResponse
import PIL
from PIL import Image
# from .models import Imageo, FileUpload
from django.views.generic.base import View
from .forms3 import UploadForm, ProductForm
import tempfile

from csv import DictReader
from io import TextIOWrapper
from .models import userLogin

from .form4 import ResultForm

from .forms5 import sForm

from .tmpform import UploadFileForm
from django.contrib import messages




class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "NEC/upload.html", {"form": UploadForm()})

    def post(self, request, *args, **kwargs):
        products_file = request.FILES["products_file"]
        rows = TextIOWrapper(products_file, encoding="utf-8", newline="")
        row_count = 0
        form_errors = []

        for row in DictReader(rows):
            row_count += 1
            form = ProductForm(row)
            if not form.is_valid():
                form_errors = form_errors
                break
            form.save()
        return render(
            request,
            "NEC/upload.html",
            {
                "form": UploadForm(),
                "form_errors": form_errors,
                "row_count": row_count,
            }
        )


def userDb(request):     
    form=ResultForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        objects = userLogin.objects.filter(symb=form.cleaned_data['symb'], dob=form.cleaned_data['dob'])
        context ['objects'] = objects
    
    return render(request, 'NEC/UserDatabase.html', context)

    