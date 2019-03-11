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
