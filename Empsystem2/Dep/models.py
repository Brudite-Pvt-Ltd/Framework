from django.db import models

# creating Model class for Department


class Dep_system(models.Model):
    DepName = models.CharField(max_length=80, unique=True)
    Department_Head = models.CharField(max_length=80)

    def __str__(self):
        return self.DepName
