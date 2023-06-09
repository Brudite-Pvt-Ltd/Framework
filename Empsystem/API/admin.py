from django.contrib import admin
from .models import Emp_system, Dep_system
# Register your models here.


@admin.register(Emp_system)
class EmpsystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Salary',
                    'Description', 'Designation', 'Manager', 'DepName']


@admin.register(Dep_system)
class DepSystemAdmin(admin.ModelAdmin):
    list_display = ['DepName', 'Department_Head']
