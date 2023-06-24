from django.urls import include
from django.contrib import admin
from django.urls import path
from Interview_Det import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.interview_management,
         name='interview-management'),
    path('schedule-interview/', views.schedule_interview,
         name='schedule-interview'),
    path('delete-interview/', views.Delete_interview,
         name='Delete_interview'),
]
