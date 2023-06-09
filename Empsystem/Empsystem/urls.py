from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empdata/<int:pk>/', views.Emp_API),
    path('empdata/', views.Emp_API1),
    path('depdata/<int:pk>/', views.Dep_API)


]
