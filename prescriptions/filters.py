import django_filters
from prescriptions.models import Prescriptions

class PrescriptionFilter(django_filters.FilterSet):
    class Meta:
        model = Prescriptions
        fields = {
            'patient':['exact'],
            'doctor':['exact'],
            'start_date':['exact'],
        }
   