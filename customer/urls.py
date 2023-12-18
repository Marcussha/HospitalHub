from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create',views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.clear, name="clear"),

    path('admin', views.home, name="home"),
    path('add',views.add, name="add"),
    path('admin/edit/<int:id>', views.edit_in, name="edit_in"),
    path('admin/update/<int:id>', views.update, name="update"),
    path('admin/delete/<int:id>', views.delete, name="delete"),
]   