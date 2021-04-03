from django import forms
from django.contrib.auth.models import User
from .models import Leave


class LeaveForm (forms.ModelForm):
    class Meta:
        model=Leave
        fields= ['startdate', 'enddate', 'resumptiondate', 'leavetype']
    
    startdate = forms.DateField(
        widget=forms.TextInput( attrs={'type': 'date'} )
    )
    enddate = forms.DateField(
        widget=forms.TextInput( attrs={'type': 'date'} )
    )
    resumptiondate = forms.DateField(
        widget=forms.TextInput( attrs={'type': 'date'} )
    )