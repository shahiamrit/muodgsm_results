from django.shortcuts import render
from django.http import HttpResponse
from pyBSDate import convert_BS_to_AD
from .forms import UserInputForms
from .forms2 import ImageForm
from django.http import JsonResponse
import PIL
from PIL import Image
from .models import Imageo


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
    width = 200
    height = 200
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form1 = request.FILES
        for data in form1.values():
            img = Image.open(data)
            img = img.resize((width, height), PIL.Image.ANTIALIAS)
            img_Rgb = img.convert('RGB')
            img_Rgb.save('/home/shahiamrit365/Desktop/MUSOM Project/ENConverter/NEConverter/media/cropped_images/resize.jpg')
        return JsonResponse({'message': 'works'})

    
    fm = UserInputForms()
    if request.method == 'POST':
        up = request.POST.get('date')
        y = up[0:4]
        m = up[5:7].lstrip('0')
        d = up[8:10]
        ad_data = convert_BS_to_AD(y, m, d)
        ad_data = str(ad_data).replace("()", "")
        return render(request, 'NEC/imgCon.html', {'fmr': fm, 'dt': ad_data})


    context = {'form': form, 'fmr': fm}
    return render(request, 'NEC/imgCon.html', context)

def conId(request, pk):
    data = Imageo.objects.get(pk=pk)
    print(data)
    return HttpResponse("hi")
