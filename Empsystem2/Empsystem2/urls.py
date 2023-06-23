
from django.contrib import admin
from django.urls import path
from Dep import views as v1
from Emp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path for Department Api and Employee API
    path('depdata/<int:pk>/', v1.Dep_API),
    path('empdata/<int:pk>/', v2.Emp_API),
    path('managerdata/', v2.Manager_API),
    # Path for Retrieving Employee under one department
    path('allemp/<str:DN>/', v1.AllEmp),
    # Path specifies for getting sum salary of all employees under one department
    path('AllEmpSalary/<str:DN>', v1.AllEmpSalary),
    # Path for Retrieving Employee under one Manager
    path('allempmanager/<str:Mana>/', v2.AllEmpManager),
    # Path specifies for getting top 3 salary of all employees under one department
    path('topsalary/<str:DN>', v1.Top3Salary),
    path('topsalarya/<str:DN>', v1.Top3Salarya),
]
