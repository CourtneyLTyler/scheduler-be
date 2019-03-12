from django.db import models
from datetime import datetime


POSITION_CHOICES = (
    ('server', 'Server'),
    ('host', 'Host'),
    ('bartender', 'Bartender')
)


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=20, choices=POSITION_CHOICES, default='server')
    photo_url = models.TextField()
    sales = models.IntegerField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


MANAGER_CHOICES = (
    ('manager', 'Manager'),
    ('general_manager', 'General Manager'),
    ('assistant_manager', 'Assistant Manager')
)


class Manager(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=30, choices=MANAGER_CHOICES, default='manager')
    photo_url = models.TextField()

    def __str__(self):
        return self.full_name


COLOR_CHOICES = (
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('purple', 'Purple')
)


SHIFT_CHOICES = (
    ('AM', 'Morning Shift'),
    ('AFT', 'Afternoon Shift'),
    ('PM', 'Evening Shift')
)


class Section(models.Model):
    date = models.DateField(blank=True, null=True)
    shift = models.CharField(
        max_length=30, choices=SHIFT_CHOICES, default='AM')
    color = models.CharField(
        max_length=20, choices=COLOR_CHOICES, default='red')
    num_of_tables = models.IntegerField()

    def __str__(self):
        return self.color


DEFAULT_EMPLOYEE_ID = 1


class ScheduleByShift(models.Model):
    date = models.DateField(blank=True, null=True)
    shift = models.CharField(max_length=30, choices=SHIFT_CHOICES)
    num_of_sections = models.IntegerField()

    section_red = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='red', default=DEFAULT_EMPLOYEE_ID)

    section_orange = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='orange', default=DEFAULT_EMPLOYEE_ID)

    section_yellow = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='yellow', default=DEFAULT_EMPLOYEE_ID)

    section_green = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='green', default=DEFAULT_EMPLOYEE_ID)

    section_blue = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='blue', default=DEFAULT_EMPLOYEE_ID)

    section_purple = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='purple', default=DEFAULT_EMPLOYEE_ID)

    def __repr__(self):
        return self.date


AVAILABILITY_CHOICES = (
    (True, 'I AM available'),
    (False, 'I am NOT available')
)


class Unavailability(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='unavailability')
    am = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)
    aft = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)
    pm = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)

    def __repr__(self):
        return self.employee


class WeeklyAvailability(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='weekly_availability')
    mon_am = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)
    mon_aft = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)
    mon_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    tue_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    tue_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    tue_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    wed_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    wed_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    wed_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    thu_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    thu_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    thu_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    fri_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    fri_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    fri_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    sat_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    sat_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    sat_pm = models.BooleanField(choices=AVAILABILITY_CHOICES, default=True)
    sun_am = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    sun_aft = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)
    sun_pm = models.BooleanField( choices=AVAILABILITY_CHOICES, default=True)

    def __repr__(self):
        return self.employee
