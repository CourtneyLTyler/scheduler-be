# from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, ManagerSerializer, SectionSerializer, ScheduleByShiftSerializer, UnavailabilitySerializer, WeeklyAvailabilitySerializer
from .models import Employee, Manager, Section, ScheduleByShift, Unavailability, WeeklyAvailability


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ScheduleByShiftList(generics.ListCreateAPIView):
    queryset = ScheduleByShift.objects.all()
    serializer_class = ScheduleByShiftSerializer

class ScheduleByShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleByShift.objects.all()
    serializer_class = ScheduleByShiftSerializer


class UnavailabilityList(generics.ListCreateAPIView):
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer

class UnavailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer


class WeeklyAvailabilityList(generics.ListCreateAPIView):
    queryset = WeeklyAvailability.objects.all()
    serializer_class = WeeklyAvailabilitySerializer

class WeeklyAvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeeklyAvailability.objects.all()
    serializer_class = WeeklyAvailabilitySerializer