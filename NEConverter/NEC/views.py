from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from pyBSDate import convert_BS_to_AD
from .forms import UserInputForms
from .forms2 import ImageForm
from django.http import JsonResponse
import PIL
from PIL import Image
from .models import Imageo, FileUpload
from django.views.generic.base import View
from .forms3 import UploadForm, ProductForm
import tempfile

from csv import DictReader
from io import TextIOWrapper
from .models import userLogin

from .form4 import ResultForm

from .forms5 import sForm

from .models import sname
from .tmpform import UploadFileForm
from django.contrib import messages

def neview(request):
    # todays's date
    fm = UserInputForms()
    if request.method == 'POST':
        up = request.POST.get('date')
        y = up[0:4]
        m = up[5:7].lstrip('0')
        d = up[8:10]
        ad_data = convert_BS_to_AD(y, m, d)
        ad_data = str(ad_data).replace("()", "")
        return render(request, 'NEC/NepaliToEnglish.html', {'fmr': fm, 'dt': ad_data})
    else:
        return render(request, 'NEC/NepaliToEnglish.html', {'fmr': fm})  


# def con(request):
#     form = ImageForm(request.POST or None, request.FILES or None)    
    
#     if form.is_valid():
#         form.save()
#         return JsonResponse({'message': 'works'})
#     context = {'form': form}
#     return render(request, 'NEC/imgCon.html', context)

def con(request):

    # Working code #
    img = Imageo.objects.latest('id')
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    fm = UserInputForms()
    if request.method == 'POST':
        up = request.POST.get('date')
        y = up[0:4]
        m = up[5:7].lstrip('0')
        d = up[8:10]
        ad_data = convert_BS_to_AD(y, m, d)
        ad_data = str(ad_data).replace("()", "")
        return render(request, 'NEC/imgCon.html', {'fmr': fm, 'dt': ad_data})

    return render(request, 'NEC/imgCon.html', {'form': form, 'img': img, 'fmr': fm})

    # working Code#

    # form = ImageForm(request.POST, request.FILES)
    # if form.is_valid():
    #     #  Open the image file
    #     image = Image.open(form.cleaned_data['file'])
    #     # Resize the image to a size of 200x200
    #     image = image.resize((200, 200), PIL.Image.ANTIALIAS)
    #     # Convert the image to the RGB format
    #     image = image.convert('RGB')
    #     # Create a temporary file
    #     with tempfile.NamedTemporaryFile(suffix='.jpg') as temp:
    #         # Save the image to the temporary file
    #         image.save(temp)
    #         # Seek to the beginning of the file
    #         temp.seek(0)
    #         # Create a new Imageo instance
    #         imageo = Imageo()
    #         # Assign the temporary file to the file field of the instance
    #         imageo.file.save('resize.jpg', temp)
    #         # Save the instance to the database
    #         imageo.save()
    #     return HttpResponse('done')
    # else:
    #     form = ImageForm()

    # img = Imageo.objects.latest('id')
    # return render(request, 'NEC/imgCon.html', {'form': form, 'img': img})






def conId(request, pk):
    data = Imageo.objects.get(pk=pk)
    print(data)
    return HttpResponse("hi")


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
    if request.method == 'POST':
        dept = request.POST.get('dept', '')
        person = request.POST.get('person', '')
        phonenumber = request.POST.get('phonenumber', '')
        if dept and person and phonenumber:
            data = sname(dept=dept, person=person, phonenumber=phonenumber)
            data.save()
            messages.success(request, '🌍 Thank you for filling out your information, with in 24 hours data entry assistant will be added in whatsapp group.')
    form=ResultForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        objects = userLogin.objects.filter(scode=form.cleaned_data['scode_no'])
        context['objects'] = objects
    return render(request, 'NEC/UserDatabase.html', context)

    


def sFormView(request):
    form = sForm(request.POST)
    if form.is_valid:
        form.save()
    return render(request, 'NEC/UserDatabase.html', {'fm': form})


def tempFileView(request):
    if request.method == 'POST' and request.FILES['formFile']:
        data = request.FILES['formFile']
        data = FileUpload(doc=data)
        data.save()
        token = data.token
        return render(request, 'NEC/tempfile.html', {'token': token})
    return render(request, 'NEC/tempfile.html')



def tempFileDownloadView(request, token):
    try:
        obj = FileUpload.objects.get(token=token)
        data = obj
        print(data.doc)
        return render(request, 'NEC/tempfile.html', {'obj': data})
    except FileUpload.DoesNotExist:
        raise Http404("File does not exist")