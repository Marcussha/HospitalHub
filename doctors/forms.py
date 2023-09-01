from django import forms
from doctors.models import Doctors

class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['doctorid', 'doctorname', 'email', 'position', 'departmentid', 'images']
        widgets = {
            'doctorid': forms.TextInput(attrs={'class': 'form-control'}),
            'doctorname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'departmentid': forms.Select(attrs={'class': 'form-control'}),
        }
