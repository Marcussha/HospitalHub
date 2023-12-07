# filters.py
import django_filters
from .models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'datebooking': ['exact'],
            'timebooking': ['exact'],
            'serviceid': ['exact'],
            'docid': ['exact'],
        }
