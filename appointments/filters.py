import django_filters
from .models import Appointment
from ministration.models import Ministration
from doctors.models import Doctors

class AppointmentFilter(django_filters.FilterSet):
    datebooking = django_filters.DateFilter(
        field_name='datebooking',
        label='Booking Date',
        lookup_expr='exact'
    )
    
    serviceid = django_filters.ModelChoiceFilter(
        field_name='serviceid',
        label='Service',
        queryset=Ministration.objects.all()  
    )
    
    docid = django_filters.ModelChoiceFilter(
        field_name='docid',
        label='Doctor',
        queryset=Doctors.objects.all()  
    )

    class Meta:
        model = Appointment
        fields = {
            'datebooking': ['exact'],
            'serviceid': ['exact'],
            'docid': ['exact'],
        }
