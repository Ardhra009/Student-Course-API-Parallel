from rest_framework import serializers
from myapp.models import StudentDB,CourseDB


class StudentSerializer(serializers.Serializer):
  student_name=serializers.CharField(max_length=100)
  email=serializers.EmailField()
  department=serializers.CharField(max_length=100)
  age=serializers.IntegerField()
class CourseSerializer(serializers.Serializer):
    course_name=serializers.CharField(max_length=100)
    duration=serializers.CharField(max_length=50)
    fee=serializers.IntegerField()
    is_active=serializers.BooleanField(default=True)
