from django.db import models


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
