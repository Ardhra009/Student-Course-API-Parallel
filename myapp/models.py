from django.db import models

# Create your models here.
class StudentDB(models.Model):
    student_name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)
    age=models.IntegerField()
class CourseDB(models.Model):
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    fee=models.IntegerField()
    is_active=models.BooleanField(default=True)
    