from astroid import objects
from django.http import HttpResponse
from django.shortcuts import redirect, render

from management.models import ClassRoom, Student
from classes.models import StudentAttendance


# Create your views here.
def index(request):
    """
        Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
    """
    search_txt = request.GET.get('inputSearch', '')
    print(search_txt)
    semester = request.GET.get('semester', '')
    year = request.GET.get('year', '')

    classes = ClassRoom.objects.filter(
        course__name__icontains=search_txt
    )
    if semester:
        classes = classes.filter(course__semester=semester)
    if year:
        classes = classes.filter(course__academic_year=year)

    return render(request, 'classes/index.html', context={
        'search_txt': search_txt,
        'semester': semester,
        'year': year,
        'classes': classes
    })

def detail(request, class_id):
    """
        Class detail page – เมื่อกด link จากหน้า Index page มาจะได้หน้าจอแสดงรายละเอียดของแต่ละวิชา 
        (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)
    """
    classroom = ClassRoom.objects.get(pk=class_id)
    attend_amount = classroom.students.count()
    absent_amount = classroom.student_amount - attend_amount
    return render(request, 'classes/detail.html', context={
        'classroom': classroom,
        'attend': attend_amount,
        'absent': absent_amount
    })

def check_in(request, class_id):
    """
        Check-in page - เมื่อกดปุ่ม Check in ในหน้า Course detail page จะทำการบันทึกกว่าเช็คชื่อเข้าเรียน 
        (ให้ใช้ student ที่มี id = 1 เสมอทุกครั้งที่กด Check in เนื่องจากเรายังไม่ได้เรียนเกี่ยวกับการจัดการ login logout และ user ของ Django)
        โดยถ้ากดปุ่ม Check in ซ้ำจะเป็นการไปบันทึกเวลาใหม่ในรายการเดิม
    """
    student = Student.objects.get(pk=1)
    attend = StudentAttendance.objects.create(
        classroom_id=class_id,
        student_id=student.id,
        attend=True
    )

    return redirect(to='class_detail', class_id=class_id)