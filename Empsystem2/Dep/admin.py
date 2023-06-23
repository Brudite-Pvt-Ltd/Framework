# Importing necessary dependencies
from django.contrib import admin
from .models import Dep_system
from Emp.models import Emp_system

# Registering admin for the Department by ModelAdmin


@admin.register(Dep_system)
class DepSystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'DepName', 'Department_Head']
