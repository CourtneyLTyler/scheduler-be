from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    url('employees', views.EmployeeList.as_view(), name='employee-list'),
    url('managers', views.ManagerList.as_view(), name='manager-list'),
    url('sections', views.SectionList.as_view(), name='section-list'),
    # url('employee/<int:pk>', views.EmployeeDetail.as_view(), name='employee-detail'),
]

# # todos/urls.py
# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.EmployeeList.as_view()),
#     # path('<int:pk>/', views.DetailEmployee.as_view()),
# ]
