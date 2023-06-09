
from django.contrib import admin
from django.urls import path
from Dep import views as v1
from Emp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depdata/', v1.Dep_API),
    path('empdata/', v2.Emp_API)
]
