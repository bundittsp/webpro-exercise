from django.http import HttpResponse
from django.shortcuts import render, redirect
from management.models import Student

# Create your views here.
def index(request):
    """
        Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
    """
    search_txt = request.GET.get('inputSearch')
    print(search_txt)
    return render(request, 'classes/index.html', context={
        'search_txt': search_txt
    })

def detail(request, class_id):
    """
        Class detail page – เมื่อกด link จากหน้า Index page มาจะได้หน้าจอแสดงรายละเอียดของแต่ละวิชา 
        (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)
    """
    return render(request, 'classes/detail.html', context={})

def check_in(request, class_id):
    """
        Check-in page - เมื่อกดปุ่ม Check in ในหน้า Course detail page จะทำการบันทึกกว่าเช็คชื่อเข้าเรียน 
        (ให้ใช้ student ที่มี id = 1 เสมอทุกครั้งที่กด Check in เนื่องจากเรายังไม่ได้เรียนเกี่ยวกับการจัดการ login logout และ user ของ Django)
        โดยถ้ากดปุ่ม Check in ซ้ำจะเป็นการไปบันทึกเวลาใหม่ในรายการเดิม
    """
    student = Student.objects.get(pk=1)

    return redirect(to='class_detail', class_id=class_id)