from django.shortcuts import render,HttpResponse
from app.forms import *

# Create your views here.
def rform(request):
    ETFO=DetailsForm()
    d={'ETFO':ETFO}
    if request.method=='POST' and request.FILES:
        DFDO=DetailsForm(request.POST,request.FILES)
        DFDO.save()
        return HttpResponse('User Resister Sucessfully')

    return render(request,'form.html',d)

