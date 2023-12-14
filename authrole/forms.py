from django import forms  
from .models import AuthUserGroups
class UserGroupsForm(forms.ModelForm):  
    class Meta:  
        model = AuthUserGroups  
        fields = [ 'user', 'group'] 
        widgets = { 'user': forms.Select(attrs={ 'class': 'form-control', 'style': 'width: 100%' }), 
                   'group': forms.Select(attrs={ 'class': 'form-control', 'style': 'width: 100%' }),
        }   