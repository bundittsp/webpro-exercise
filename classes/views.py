from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    """
        Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
    """
    return HttpResponse('Index')

def detail(request, class_id):
    """
        Course detail page – เมื่อกด link จากหน้า Index page มาจะได้หน้าจอแสดงรายละเอียดของแต่ละวิชา 
        (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)
    """
    return HttpResponse('Class Detail: %s' % class_id)

def check_in(request, class_id):
    """
        Check-in page - เมื่อกด link จากหน้า Index page หรือ Course detail page ก็จะพบหน้าจอที่มีชื่อคอร์สอยู่เป็นหัวข้อ 
        และมี QR code (เป็นรูป static หามาจาก Internet ไม่ต้อง auto-generate)
    """
    return HttpResponse('Attendance Check-in: %s' % class_id)