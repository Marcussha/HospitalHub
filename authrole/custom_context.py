from django.contrib.auth.models import Group

def custom_context(request):
    is_admin = request.user.groups.filter(name='Admin').exists()
    is_doctor = request.user.groups.filter(name='Doctor').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()

    return {
        'is_admin': is_admin,
        'is_doctor': is_doctor,
        'is_manager': is_manager,
    }
