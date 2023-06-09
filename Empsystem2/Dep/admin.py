from django.contrib import admin
from .models import Dep_system


@admin.register(Dep_system)
class DepSystemAdmin(admin.ModelAdmin):
    list_display = ['DepName', 'Department_Head']
