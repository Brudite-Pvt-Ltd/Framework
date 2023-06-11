from django.contrib import admin
from .models import Emp_system

# Registering admin for the Department by ModelAdmin


@admin.register(Emp_system)
class EmpSystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Salary',
                    'Description', 'Designation', 'Manager', 'DepName']
