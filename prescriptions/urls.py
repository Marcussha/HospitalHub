from django.contrib import admin
from django.urls import path 
from prescriptions import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('/create',views.create, name="create"),
    path('/edit/<int:id>', views.edit, name="edit"),
    path('/update/<int:id>', views.update, name="update"),
    path('/delete/<int:id>', views.delete, name="delete")
]
