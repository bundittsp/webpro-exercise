from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    semester = models.CharField(max_length=1)
    academic_year = models.CharField(max_length=4)