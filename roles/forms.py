from django import forms  
from roles.models import AuthGroup 
class RoleForm(forms.ModelForm):  
    class Meta:  
        model = AuthGroup  
        fields = [ 'name'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
        }   