from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    """
        Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
    """
    classes = models.classes
    courses = models.courses
    for cl in classes:
        cl['course'] = [co for co in courses if co['id'] == cl['course_id']][0]
    
    context = {
        'new_classes': classes
    }
    return render(request, 'attedance/index.html', context=context)

def detail(request, class_id):
    """
        Class detail page – เมื่อกด link จากหน้า Index page มาจะได้หน้าจอแสดงรายละเอียดของแต่ละวิชา 
        (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)
    """
    courses = models.courses
    classes = models.classes
    attends = models.attendance

    sel_class = [cl for cl in classes if cl['id'] == class_id][0]
    sel_course = [co for co in courses if co['id'] == sel_class['course_id']][0]
    sel_attend = [att for att in attends if att['class_id'] == class_id][0]
    
    context = {
        'sel_class': sel_class,
        'sel_course': sel_course,
        'sel_attend': sel_attend
    }
    return render(request, 'classes/detail.html', context=context)

def check_in(request, class_id):
    """
        Check-in page - เมื่อกด link จากหน้า Index page หรือ Course detail page ก็จะพบหน้าจอที่มีชื่อคอร์สอยู่เป็นหัวข้อ 
        และมี QR code (เป็นรูป static หามาจาก Internet ไม่ต้อง auto-generate)
    """
    courses = models.courses
    classes = models.classes

    sel_class = [cl for cl in classes if cl['id'] == class_id][0]
    sel_course = [co for co in courses if co['id'] == sel_class['course_id']][0]
    context = {
        'sel_class': sel_class,
        'sel_course': sel_course
    }
    return render(request, 'classes/checkin.html', context=context)