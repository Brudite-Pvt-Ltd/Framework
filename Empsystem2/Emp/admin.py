from django.contrib import admin
from .models import Emp_system


@admin.register(Emp_system)
class EmpSystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Salary',
                    'Description', 'Designation', 'Manager', 'DepName']
