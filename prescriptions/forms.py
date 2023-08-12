from django import forms
from prescriptions.models import Prescriptions

class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = ['prescriptionid', 'name_diseaase', 'symptoms', 'date', 'medicine', 'note', 'userid', 'doctorid', 're_examination_date']
        widgets = {
            'prescriptionid': forms.TextInput(attrs= {'class':'form-control'}),
            'name_diseaase': forms.TextInput(attrs={'class':"form-control"}),
            'symptoms': forms.TextInput(attrs={'class':"form-control"}),
            'date': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'medicine':forms.TextInput(attrs={'class':'form-control'}),
            'note': forms.TextInput(attrs={'class':'form-control'}),
            'userid': forms.Select(attrs={'class':'form-control'}),
            'doctorid':forms.Select(attrs={'class':'form-control'}),
            're_examination_date': forms.SelectDateWidget(attrs={'class':'form-control'}),
        }