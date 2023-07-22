from django import forms  
from role.models import Roles 
class RoleForm(forms.ModelForm):  
    class Meta:  
        model = Roles  
        fields = [ 'roleid','rolename'] 
        widgets = { 'roleid': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'rolename': forms.TextInput(attrs={ 'class': 'form-control' }), 
        }   