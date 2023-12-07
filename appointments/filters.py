# filters.py
import django_filters
from .models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'fullname': ['icontains'],
            'email': ['icontains'],
            'phone': ['icontains'],
            'datebooking': ['exact'],
            'timebooking': ['exact'],
            'serviceid': ['exact'],
            'docid': ['exact'],
            'note': ['icontains'],
        }
