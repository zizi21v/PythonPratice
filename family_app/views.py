from hashlib import new
from django.shortcuts import render
from family_app.models import familyInfo
import datetime

def create_info(request):
    d = datetime.date(1980, 2, 25)
    new_info = familyInfo.objects.create(nombre="Jorge", edad=42, cumpleaños= d)
    context = {
        'new_info':new_info
    }
    return render(request,'template.html', context=context)


def list_Family(request):
    familyMembers = familyInfo.objects.all()
    context = {
        'familyMembers': familyMembers
    }
    return render(request, 'familylist.html', context=context)



