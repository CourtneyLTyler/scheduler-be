from django.conf.urls import url
from django.urls import path

# from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('employees', views.EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>', views.EmployeeDetail.as_view(), name='employee-detail'),

    path('managers', views.ManagerList.as_view(), name='manager-list'),
    path('manager/<int:pk>', views.ManagerDetail.as_view(), name='manager-detail'),

    path('sections', views.SectionList.as_view(), name='section-list'),
    path('section/<int:pk>', views.SectionDetail.as_view(), name='section-detail'),

    path('schedulebyshifts', views.ScheduleByShiftList.as_view(), name='schedule-by-shift-list'),
    path('schedulebyshift/<int:pk>', views.ScheduleByShiftDetail.as_view(), name='schedule-by-shift-detail'),

    path('unavailability', views.UnavailabilityList.as_view(),
    name='unavailability-list'),
    path('unavailability/<int:pk>', views.UnavailabilityDetail.as_view(), name='unavailability-detail'),

    path('weeklyavailability', views.WeeklyAvailabilityList.as_view(),
    name='weeklyavailability-list'),
    path('weeklyavailability/<int:pk>', views.WeeklyAvailabilityDetail.as_view(), name='weeklyavailability-detail'),
]