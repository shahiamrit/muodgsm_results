from django.shortcuts import render
from django.http import HttpResponse
from pyBSDate import convert_BS_to_AD
from . forms import UserInputForms
def neview(request):
    # todays's date
    fm = UserInputForms()
    if request.method == 'POST':
        data = request.POST.get('date')
        up = data.replace('-',',')
        y = up[0:4]
        m = up[5:7].lstrip('0')
        d = up[8:10]
        ad_data = convert_BS_to_AD(y, m, d)
        return HttpResponse('YYYY-MM-DD =====> ' + str(str(ad_data).replace(",","/")))

    return render(request, 'NEC/NepaliToEnglish.html', {
            'fmr': fm,
            # 'dt': ad_data
        })  