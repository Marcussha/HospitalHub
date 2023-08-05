from django import forms
from appointments.models import Appointment

class AppointmentForm (forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['appointmentid','datebooking','note','customerid','serviceid','docid']
        widgets = {'appointmentid': forms.TextInput(attrs={'class': 'form-control'}),
                    'datebooking': forms.SelectDateWidget(attrs={'class':'form-control'}),
                    'note': forms.TextInput(attrs={'class':'form-control'}),
                    'customerid': forms.Select(attrs={'class':'form-control'}),
                    'serviceid': forms.Select(attrs={'class':'form-control'}),
                    'docid': forms.Select(attrs={'class':'form-control'}),
                    }