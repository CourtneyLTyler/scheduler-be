# from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, ManagerSerializer, SectionSerializer, ScheduleByShiftSerializer, UnavailabilitySerializer, WeeklyAvailabilitySerializer
from .models import Employee, Manager, Section, ScheduleByShift, Unavailability, WeeklyAvailability


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ScheduleByShiftList(generics.ListCreateAPIView):
    queryset = ScheduleByShift.objects.all()
    serializer_class = ScheduleByShiftSerializer


class UnavailabilityList(generics.ListCreateAPIView):
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer


class WeeklyAvailabilityList(generics.ListCreateAPIView):
    queryset = WeeklyAvailability.objects.all()
    serializer_class = WeeklyAvailabilitySerializer
