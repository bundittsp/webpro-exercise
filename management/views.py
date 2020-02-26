from astroid import objects
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from management.models import ClassRoom, Course, Room, Student


# Create your views here.
@login_required
def student_list(request):
    """
        แสดงข้อมูล student ทั้งหมดในระบบ
    """
    search = request.GET.get('search', '')

    # Document for Q objects - https://docs.djangoproject.com/en/3.0/topics/db/queries/#complex-lookups-with-q-objects
    students = User.objects.filter(
        Q(first_name__icontains=search) | 
        Q(last_name__icontains=search) | 
        Q(username__icontains=search)
    ).order_by('username')

    return render(request, 'student/student_list.html', context={
        'students': students,
        'search': search
    })

@login_required
def student_add(request):
    """
        เพิ่มข้อมูล user / student ใหม่เข้าสู่ฐานข้อมูล
    """
    msg = ''

    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            '1234',
        )
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        student = Student.objects.create(
            user=user,
            year=request.POST.get('year')
        )
        user.save()
        msg = 'Successfully create new student - username: %s' % (user.username)
    else:
        user = User.objects.none()

    context = {
        'student': user,
        'msg': msg
    }

    return render(request, 'student/student_form.html', context=context)

@login_required
def student_update(request, user_id):
    """
        Update ข้อมูลชั้นเรียนที่มี id = class_id
    """
    
    try:
        user = User.objects.get(pk=user_id)
        msg = ''
    except User.DoesNotExist:
        return redirect('student_list')

    if request.method == 'POST':
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        try:
            user.student.year=request.POST.get('year')
        except Student.DoesNotExist:
            student = Student.objects.create(
            user=user,
            year=request.POST.get('year')
        )
        user.save()
        msg = 'Successfully update student - username: %s' % (user.username)
    
    context = {
        'student': user,
        'msg': msg
    }

    return render(request, 'student/student_form.html', context=context)

@login_required
def student_delete(request, user_id):
    """
        ลบข้อมูล student โดยลบข้อมูลที่มี id = user_id
    """
    student = User.objects.get(id=user_id)
    student.is_active = False
    student.save()
    return redirect(to='student_list')

@login_required
def class_list(request):
    """
        แสดงข้อมูล classroom ทั้งหมดในระบบ
    """
    search = request.GET.get('search', '')
    classrooms = ClassRoom.objects.filter(course__name__icontains=search).order_by('course__id', 'section')
    day_dict = {v[0]: v[1] for v in ClassRoom.WEEKDAYS}
    for classroom in classrooms:
        classroom.weekday = day_dict[classroom.weekday]
    return render(request, 'class/class_list.html', context={
        'classrooms': classrooms,
        'search': search
    })

@login_required
def class_add(request):
    """
        เพิ่มข้อมูล classroom ใหม่เข้าสู่ฐานข้อมูล
    """
    courses = Course.objects.all()
    rooms = Room.objects.all()
    msg = ''

    if request.method == 'POST':
        classroom = ClassRoom.objects.create(
            course_id=request.POST.get('course_id'),
            section=request.POST.get('section'),
            weekday=request.POST.get('weekday'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            room_id=request.POST.get('room_id'),
            student_amount=request.POST.get('student_amount')
        )
        msg = 'Successfully create new classroom - id: %s' % (classroom.id)
    else:
        classroom = ClassRoom.objects.none()

    context = {
        'courses': courses,
        'weekdays': ClassRoom.WEEKDAYS,
        'rooms': rooms,
        'classroom': classroom,
        'msg': msg
    }

    return render(request, 'class/class_form.html', context=context)

@login_required
def class_update(request, class_id):
    """
        Update ข้อมูลชั้นเรียนที่มี id = class_id
    """
    
    try:
        classroom = ClassRoom.objects.get(pk=class_id)
        courses = Course.objects.all()
        rooms = Room.objects.all()
        msg = ''
    except ClassRoom.DoesNotExist:
        return redirect('class_list')

    if request.method == 'POST':
        classroom.course_id=request.POST.get('course_id')
        classroom.section=request.POST.get('section')
        classroom.weekday=request.POST.get('weekday')
        classroom.start_time=request.POST.get('start_time')
        classroom.end_time=request.POST.get('end_time')
        classroom.room_id=request.POST.get('room_id')
        classroom.student_amount=request.POST.get('student_amount')

        classroom.save()
        msg = 'Successfully update classroom - id: %s' % (classroom.id)
    
    context = {
        'courses': courses,
        'weekdays': ClassRoom.WEEKDAYS,
        'rooms': rooms,
        'classroom': classroom,
        'msg': msg
    }

    return render(request, 'class/class_form.html', context=context)

@login_required
def class_delete(request, class_id):
    """
        ลบข้อมูล classroom โดยลบข้อมูลที่มี id = class_id
    """
    classroom = ClassRoom.objects.get(id=class_id)
    classroom.delete()
    return redirect(to='class_list')