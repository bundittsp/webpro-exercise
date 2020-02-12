from django.db import models

from management.models import ClassRoom, Student

class StudentAttendance(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attend = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)