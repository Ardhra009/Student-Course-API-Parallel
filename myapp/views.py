from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp .models import StudentDB,CourseDB
from myapp.serializers import StudentSerializer,CourseSerializer
# Create your views here.
class StudentDBAPI(APIView):
    def get(self,request):
        qs=StudentDB.objects.all()
        serializer_instance=StudentSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data=request.data 
        serializer_instance=StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            StudentDB.objects.create(**actual_data)
            return Response(data={"message":"student added successfully"})
        else:
            return Response(data={"message":"invalid data"})
class StudentRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=StudentDB.objects.get(id=pk)
        serializer_instance=StudentSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):
        form_data=request.data 
        serializer_instance=StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            StudentDB.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


    def delete(self,request,pk):
        StudentDB.objects.filter(id=pk).delete()
        return Response({"message":"student deleted successfully"})

class CourseGetPost(APIView):
    def get(self,request):
        qs=CourseDB.objects.all()
        serializer_instance=CourseSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data 
        serializer_instance=CourseSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            CourseDB.objects.create(**actual_data)
            return Response(data={"message":"course added successfully"})
        else:
            return Response(data={"message":"invalid data"})

class CourseRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=CourseDB.objects.get(id=pk)
        serializer_instance=CourseSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
            form_data=request.data 
            serializer_instance=CourseSerializer(data=form_data)
            if serializer_instance.is_valid():
                actual_data=serializer_instance.validated_data
                CourseDB.objects.filter(id=pk).update(**actual_data)
                return Response(data=serializer_instance.data)
            else:
                return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        CourseDB.objects.filter(id=pk).delete()
        return Response({"message":"course deleted successfully"})
    



        


        
    
