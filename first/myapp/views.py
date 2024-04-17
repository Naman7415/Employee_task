from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import filters
from rest_framework import generics

# Create your views here.



from rest_framework.viewsets import ModelViewSet

class EmployeeView(ModelViewSet):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer
    
    

class UserListView(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['EmployeeName__icontains']
    