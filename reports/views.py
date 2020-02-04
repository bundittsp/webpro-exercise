from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return HttpResponse('Dashboard Page.')

def search(request):
    return HttpResponse('Attendance Search Page.')