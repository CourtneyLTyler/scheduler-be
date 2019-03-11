from django.db import models


POSITION_CHOICES = (
('server', 'Server'),
('host', 'Host'),
('bartender', 'Bartender')
)

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='server')
    photo_url = models.TextField()
    # need to check how to link this
    # availability = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='availability')
    # unavailability = models.ForeignKey(Unavailability, on_delete=models.CASCADE, related_name='unavailability')
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
    position = models.CharField(max_length=30, choices=MANAGER_CHOICES, default='manager')
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

class Section(models.Model):
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='red')
    num_of_tables = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='section')

    def __str__(self):
        return self.color


DAYOFWEEK_CHOICES = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday')
)

class ScheduleByDay(models.Model):
    date = models.DateField()
    day_of_week = models.CharField(max_length=20, choices=DAYOFWEEK_CHOICES, default='monday')
    am_staff_num = models.IntegerField()
    aft_staff_num = models.IntegerField()
    pm_staff_num = models.IntegerField()
    am_sec_num = models.IntegerField()
    aft_sec_num = models.IntegerField()
    pm_sec_num = models.IntegerField()

    def __str__(self):
        return self.date

AVAILABILITY_CHOICES = (
    ('available', 'I AM available'),
    ('unavailable', 'I am NOT available')
)


class Unavailability(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='unavailability')
    am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.employee


class WeeklyAvailability(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='weekly_availability')
    mon_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    mon_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    mon_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_am = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_aft = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_pm = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.employee
