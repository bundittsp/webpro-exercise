from astroid import objects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from classes.models import StudentAttendance
from management.models import ClassRoom, Student


# Create your views here.
def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
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

@login_required
def detail(request, class_id):
    """
        Class detail page – เมื่อกด link จากหน้า Index page มาจะได้หน้าจอแสดงรายละเอียดของแต่ละวิชา 
        (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)
    """
    student = request.user.student
    classroom = ClassRoom.objects.get(pk=class_id)
    checked = StudentAttendance.objects.filter(classroom_id=class_id, student_id=student.id).exists()
    attend_amount = classroom.students.count()
    absent_amount = classroom.student_amount - attend_amount
    return render(request, 'classes/detail.html', context={
        'classroom': classroom,
        'attend': attend_amount,
        'absent': absent_amount,
        'checked': checked
    })

@login_required
def check_in(request, class_id):
    """
        Check-in page - เมื่อกดปุ่ม Check in ในหน้า Course detail page จะทำการบันทึกกว่าเช็คชื่อเข้าเรียน
        โดยถ้ากดปุ่ม Check in ซ้ำจะเป็นการไปบันทึกเวลาใหม่ในรายการเดิม
    """
    student = request.user.student
    if not StudentAttendance.objects.filter(classroom_id=class_id, student_id=student.id).exists():
        attend = StudentAttendance.objects.create(
            classroom_id=class_id,
            student_id=student.id,
            attend=True
        )

    return redirect(to='class_detail', class_id=class_id)