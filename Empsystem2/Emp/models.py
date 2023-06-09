from django.db import models
from Dep.models import Dep_system


class Emp_system(models.Model):

    Name = models.CharField(max_length=80)
    Salary = models.FloatField()
    Description = models.CharField(max_length=80)
    Designation = models.CharField(max_length=80)
    Manager = models.CharField(max_length=70)
    DepName = models.ForeignKey(Dep_system, on_delete=models.CASCADE)
