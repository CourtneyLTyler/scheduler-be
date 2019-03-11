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


class WeeklyAvailability(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee')
    monAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    monAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    monPM = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tueAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tueAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    tuePm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wedAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wedAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    wedPm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thuAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thuAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    thuPm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    friAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    friAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    friPm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    satAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    satAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    satPm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sunAm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sunAft = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
    sunPm = models.CharField(max_length=20, required=True, choices=set(
        ["I am available", "I am not available"]))
