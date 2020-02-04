from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Index')

def detail(request, class_id):
    return HttpResponse('Class Detail: %s' % class_id)

def check_in(request, class_id):
    return HttpResponse('Attendance Check-in: %s' % class_id)