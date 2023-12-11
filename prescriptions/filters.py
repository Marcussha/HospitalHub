import django_filters
from prescriptions.models import Prescriptions
from customer.models import Client
from doctors.models import Doctors
from django import forms

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    
class CustomSelect(forms.Select):
    pass

class PrescriptionFilter(django_filters.FilterSet):
    patient = django_filters.ModelChoiceFilter(
        field_name = 'patient',
        label="Patient",
        queryset=Client.objects.all(),
        widget=CustomSelect(attrs={'class':"form-control"}) 
    )
    
    doctor = django_filters.ModelChoiceFilter(
        field_name="doctor",
        label="Doctor",
        queryset=Doctors.objects.all(),
        widget=CustomSelect(attrs={'class':"form-control"})
    )
    
    start_date = django_filters.DateFilter(
        field_name="start_date",
        label="Start Date",
        lookup_expr="exact",
        widget=CustomDateInput(attrs={'class':'form-control'})
    )
    
    re_examination_date = django_filters.DateFilter(
        field_name="re_examination_date",
        label="Re-Examination Date",
        lookup_expr="exact",
        widget=CustomDateInput(attrs={'class':'form-control'})
    )
    class Meta:
        model = Prescriptions
        fields = {
            'patient':['exact'],
            'doctor':['exact'],
            'start_date':['exact'],
            're_examination_date':['exact']
        }