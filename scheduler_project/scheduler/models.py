from django.db import models


class ScheduleByDay(models.Model):
    date = models.DateField()
    dayOfWeek = models.CharField(max_length=100)
    amStaffNum = models.IntegerField()
    aftStaffNum = models.IntegerField()
    pmStaffNum = models.IntegerField()
    amSecNum = models.IntegerField()
    aftSecNum = models.IntegerField()
    pmSecNum = models.IntegerField()


class Unavailability(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee')
    am = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    aft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    pm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
