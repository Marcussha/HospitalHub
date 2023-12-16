from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin', views.index, name="index"),
    path('index', views.static, name="static"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('signout', views.signout, name="signout"),
    path('profile', views.profile, name='profile'),
    path('profile/edit/',views.edit_profile, name='edit_profile'),

]