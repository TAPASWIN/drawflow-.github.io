# configurator/forms.py
from django import forms

class ComputerConfigurationForm(forms.Form):
    address = forms.CharField(max_length=255, label='Address')
    json_config = forms.CharField(widget=forms.HiddenInput())
