from django.db import models

class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=20, required=True, choices=set(["server", "host", "bartender"]))
    photo_url = models.TextField()
    # need to check how to link this
    # availability = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='availability')
    # unavailability = models.ForeignKey(Unavailability, on_delete=models.CASCADE, related_name='unavailability')
    sales = models.IntegerField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.fullName


class Manager(models.Model):
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.fullName


class FloorPlan(models.Model):
    # need to link to sections table
    num_of_sections = models.IntegerField()
        # not sure about this
    def __str__(self):
        return self.num_of_sections


class Section(models.Model):
    color = models.CharField(max_length=20, required=True, choices=set(['red', 'orange', 'yellow', 'green', 'blue', 'purple']))
    num_of_tables = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.color
