from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=10)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    semester = models.CharField(max_length=1) # ภาคเรียน
    academic_year = models.CharField(max_length=4) # ปีการศึกษา


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.SmallIntegerField() # ชั้นปี


class ClassRoom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    section = models.SmallIntegerField()
    WEEKDAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('TH', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
        ('Su', 'Sunday'),
    )
    weekday = models.CharField(max_length=2, choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    student_amount = models.IntegerField(default=0) # จำนวน นศ. ที่ลงทะเบียนทั้งหมด
    students = models.ManyToManyField(
        Student, 
        through='classes.StudentAttendance'
    )