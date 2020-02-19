from astroid import objects
from django.http import HttpResponse
from django.shortcuts import redirect, render

from management.models import ClassRoom


# Create your views here.
def student_list(request):
    return HttpResponse('List Student Page.')

def student_add(request):
    return HttpResponse('Add Student Page.')

def student_delete(request, student_id):
    return HttpResponse('Delete Student Page.')

def class_list(request):
    """
        แสดงข้อมูล classroom ทั้งหมดในระบบ
    """
    classrooms = ClassRoom.objects.all()
    day_dict = {v[0]: v[1] for v in ClassRoom.WEEKDAYS}
    for classroom in classrooms:
        classroom.weekday = day_dict[classroom.weekday]
    return render(request, 'management/class_list.html', context={
        'classrooms': classrooms
    })

def class_add(request):
    """
        เพิ่มข้อมูล classroom ใหม่เข้าสู่ฐานข้อมูล
    """
    return render(request, 'management/class_add.html')

def class_delete(request, class_id):
    """
        ลบข้อมูล classroom โดยลบข้อมูลที่มี id = class_id
    """
    classroom = ClassRoom.objects.get(id=class_id)
    classroom.delete()
    return redirect(to='class_list')