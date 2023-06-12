from django.db import models
from Dep.models import Dep_system

# creating Model class for Department


class Manager_Mod(models.Model):
    Manager = models.CharField(max_length=50, primary_key=True, unique=True)


class Emp_system(models.Model):

    Name = models.CharField(max_length=80)
    Salary = models.FloatField()
    Description = models.CharField(max_length=80)
    Designation = models.CharField(max_length=80)
    Manager = models.ForeignKey(Manager_Mod, on_delete=models.CASCADE)
    DepName = models.ForeignKey(Dep_system, on_delete=models.CASCADE)
