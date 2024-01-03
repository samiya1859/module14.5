from django import forms 

from secondapp.models import User2

class UserForm(forms.ModelForm):
    class Meta:
        model = User2
        fields='__all__'