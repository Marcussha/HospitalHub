from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/home', views.home, name="home"),
    path('/create',views.create, name="create_appointment"),
    path('/delete/<int:id>', views.clear, name="clear"),
    path('/excel/', views.export_excel, name='export_excel'),
    path('/csv/', views.export_csv, name='export_csv'),
    path('/export_filtered_excel/', views.export_filtered_excel, name="export_filtered_excel"),
]