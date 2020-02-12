from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    semester = models.CharField(max_length=1)
    academic_year = models.CharField(max_length=4)


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
    room = models.CharField(max_length=10)
    student_amount = models.IntegerField(default=0)
