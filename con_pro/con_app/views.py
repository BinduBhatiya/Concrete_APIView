from django.shortcuts import render
from .models import student
from .serializers import studentserializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class StudentListCreate(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializers

# retrive, update and destroy : id is required
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializers
    