from django import forms 
from departments.models import Departments
class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['departmentid', 'named']
        widgets = {'deparmentid': forms.TextInput(attrs={'class': 'form-control'}),
                   'named': forms.TextInput(attrs={'class':'form-control'}),
                   }