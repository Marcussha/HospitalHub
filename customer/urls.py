from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/create',views.create, name="create"),
    path('/delete/<int:id>', views.clear, name="clear"),
    path('/get_client_data/', views.get_client_data, name='get_client_data'),
]   