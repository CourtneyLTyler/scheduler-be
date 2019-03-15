# from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, ManagerSerializer, SectionSerializer, ScheduleByShiftSerializer, UnavailabilitySerializer, WeeklyAvailabilitySerializer
from .models import Employee, Manager, Section, ScheduleByShift, Unavailability, WeeklyAvailability
from rest_framework.permissions import AllowAny


class EmployeeList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class SectionList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ScheduleByShiftList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = ScheduleByShift.objects.all()
    serializer_class = ScheduleByShiftSerializer


class ScheduleByShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = ScheduleByShift.objects.all()
    serializer_class = ScheduleByShiftSerializer


class UnavailabilityList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer


class UnavailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer


class WeeklyAvailabilityList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = WeeklyAvailability.objects.all()
    serializer_class = WeeklyAvailabilitySerializer


class WeeklyAvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = WeeklyAvailability.objects.all()
    serializer_class = WeeklyAvailabilitySerializer
