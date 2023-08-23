from django import forms
from appointments.models import Appointment

class AppointmentForm (forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['appid','fullname','email','phone','datebooking','serviceid','docid','note']
        widgets = {'appid': forms.TextInput(attrs={'class': 'form-control'}),
                    'fullname': forms.TextInput(attrs={'class':'form-control'}),
                    'email': forms.EmailInput(attrs={'class':'form-control'}),
                    'phone': forms.TextInput(attrs={'class':'form-control'}),
                    'datebooking': forms.SelectDateWidget(attrs={'class':'form-control'}),
                    'serviceid': forms.Select(attrs={'class':'form-control'}),
                    'docid': forms.Select(attrs={'class':'form-control'}),
                    'note': forms.TextInput(attrs={'class':'form-control'}),                    
                    }