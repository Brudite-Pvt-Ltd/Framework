from django.contrib import admin
from .models import Emp_system, Manager_Mod

# Registering admin for the Department by ModelAdmin


@admin.register(Manager_Mod)
class ManagerModAdmin(admin.ModelAdmin):
    list_display = ['Manager']


@admin.register(Emp_system)
class EmpSystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Salary',
                    'Description', 'Designation', 'Manager', 'DepName']
