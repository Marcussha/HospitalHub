from django.contrib import admin
from django.urls import path 
from doctors import views 

urlpatterns = [
     path('', views.index, name='index'),
     path('/create', views.create, name='create'),
     path('/delete/<int:id>', views.clear, name='clear'),
     path('/edit/<int:id>', views.edit, name='edit'), 
 ]
 