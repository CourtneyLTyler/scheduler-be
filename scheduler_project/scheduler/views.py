# from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, ManagerSerializer, SectionSerializer
from .models import Employee, Manager, Section


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
