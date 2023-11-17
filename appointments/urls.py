from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/create',views.create, name="create_appointment"),
    path('/delete/<int:id>', views.clear, name="clear"),
    path('/excel/', views.export_excel, name='export_excel'),
    path('/csv/', views.export_csv, name='export_csv'),
    path('/calendar/', views.display_appointments, name='display_appointments'),
]