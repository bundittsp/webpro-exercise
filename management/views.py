from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def student_list(request):
    return HttpResponse('List Student Page.')

def student_add(request):
    return HttpResponse('Add Student Page.')

def student_update(request, student_id):
    return HttpResponse('Update Student Page.')

def class_list(request):
    return HttpResponse('List Class Page.')

def class_add(request):
    return HttpResponse('Add Class Page.')

def class_update(request, class_id):
    return HttpResponse('Update Class Page.')

