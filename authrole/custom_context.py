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

# Apply the decorator to a view function
@user_passes_test(user_is_admin)
def admin_view(request):
    # Your view logic here
    return render(request, 'admin_template.html')

@user_passes_test(user_is_doctor)
def doctor_view(request):
    # Your view logic here
    return render(request, 'doctor_template.html')

@user_passes_test(user_is_manager)
def manager_view(request):
    # Your view logic here
    return render(request, 'manager_template.html')