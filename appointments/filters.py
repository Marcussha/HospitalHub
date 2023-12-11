import django_filters
from .models import Appointment
from ministration.models import Ministration
from doctors.models import Doctors
from .forms import forms

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    
class CustomSelect(forms.Select):
    pass

class AppointmentFilter(django_filters.FilterSet):
    datebooking = django_filters.DateFilter(
        field_name='datebooking',
        label='Booking Date',
        lookup_expr='exact',
        widget=CustomDateInput(attrs={'class': 'form-control'})
    )
    
    serviceid = django_filters.ModelChoiceFilter(
        field_name='serviceid',
        label='Service',
        queryset=Ministration.objects.all(),  
        widget=CustomSelect(attrs={'class':"form-control"})
    )
    
    docid = django_filters.ModelChoiceFilter(
        field_name='docid',
        label='Doctor',
        queryset=Doctors.objects.all(),  
        widget=CustomSelect(attrs={'class':"form-control"})
    )

    class Meta:
        model = Appointment
        fields = {
            'datebooking': ['exact'],
            'serviceid': ['exact'],
            'docid': ['exact'],
        }