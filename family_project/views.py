from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def family(request):
    return HttpResponse('Hola Mundo!')
