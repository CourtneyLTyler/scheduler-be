from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, required=True, choices=set(["server", "host", "bartender"]))
    photo_url = models.TextField()
    # need to check how to link this
    # availability = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='availability')
    # unavailability = models.ForeignKey(Unavailability, on_delete=models.CASCADE, related_name='unavailability')
    sales = models.IntegerField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Manager(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=30, required=True, choices=set(["manager", "general manager", "assistant manager"]))
    photo_url = models.TextField()

    def __str__(self):
        return self.full_name


class FloorPlan(models.Model):
    num_of_sections = models.IntegerField()

    def __str__(self):
        return self.num_of_sections


class Section(models.Model):
    color = models.CharField(max_length=20, required=True, choices=set(['red', 'orange', 'yellow', 'green', 'blue', 'purple']))
    num_of_tables = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='section')

    def __str__(self):
        return self.color

class ScheduleByDay(models.Model):
    date = models.DateField()
    day_of_week = models.CharField(max_length=100)
    am_staff_num = models.IntegerField()
    aft_staff_num = models.IntegerField()
    pm_staff_num = models.IntegerField()
    am_sec_num = models.IntegerField()
    aft_sec_num = models.IntegerField()
    pm_sec_num = models.IntegerField()

    def __str__(self):
        return self.date


class Unavailability(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='unavailability')
    am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))

    def __str__(self):
        return self.employee


class WeeklyAvailability(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='weekly_availability')
    mon_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    mon_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    mon_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tue_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tue_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tue_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wed_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wed_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wed_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thu_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thu_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thu_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    fri_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    fri_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    fri_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sat_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sat_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sat_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sun_am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sun_aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sun_pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))

    def __str__(self):
        return self.employee
