
from django.contrib import admin
from django.urls import path
from Dep import views as v1
from Emp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path for Department Api and Employee API
    path('depdata/', v1.Dep_API),
    path('empdata/', v2.Emp_API),
    # Path for Retrieving Employee under one department
    path('allemp/<str:DN>', v1.AllEmp),
    # Path specifies for getting sum salary of all employees under one department
    path('AllEmpSalary/<str:DN>', v1.AllEmpSalary),
    # path('allemp2/', v2.AllEmp)
]
