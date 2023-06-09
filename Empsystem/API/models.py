from django.db import models


class Dep_system(models.Model):
    DepName = models.CharField(max_length=80)
    Department_Head = models.CharField(max_length=80)


class Emp_system(models.Model):

    DepName = models.ForeignKey(
        Dep_system, on_delete=models.CASCADE)
    Name = models.CharField(max_length=80)
    Salary = models.FloatField()
    Description = models.CharField(max_length=80)
    Designation = models.CharField(max_length=80)
    Manager = models.CharField(max_length=70)


# id = models.IntegerField(primary_key=True)
# Department = models.CharField(max_length=80)
# Example query for testing
# {
#     "Name":"Kanika",
#     "Salary":14000,
#     "Description":"Backend_Dev(java)",
#     "Designation":"ASE",
#     "Manager":"Ritu"
# }

# {
#     "Name":"HR",
#     "Department_Head":"Rishabh"
# }
# Dep_system object (
