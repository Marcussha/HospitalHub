from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render

def custom_context(request):
    is_admin = request.user.groups.filter(name='Admin').exists()
    is_doctor = request.user.groups.filter(name='Doctor').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()

    return {
        'is_admin': is_admin,
        'is_doctor': is_doctor,
        'is_manager': is_manager,
    }
def user_is_admin(user):
    return user.groups.filter(name='Admin').exists()

def user_is_doctor(user):
    return user.groups.filter(name='Doctor').exists()

def user_is_manager(user):
    return user.groups.filter(name='Manager').exists()
