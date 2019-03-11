from django.contrib import admin
from .models import Employee, Manager, FloorPlan, Section, ScheduleByDay, Unavailability, WeeklyAvailability

admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(FloorPlan)
admin.site.register(Section)
admin.site.register(ScheduleByDay)
admin.site.register(Unavailability)
admin.site.register(WeeklyAvailability)


