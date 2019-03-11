from django.db import models


class ScheduleByDay(models.Model):
    date = models.DateField()
    dayOfWeek: models.CharField(max_length=100)
    amStaffNum: models.IntegerField()
    aftStaffNum: models.IntegerField()
    pmStaffNum: models.IntegerField()
    amSecNum: models.IntegerField()
    aftSecNum: models.IntegerField()
    pmSecNum: models.IntegerField()
