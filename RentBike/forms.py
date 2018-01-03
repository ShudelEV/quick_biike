from django import forms
from django.forms import widgets
from datetime import datetime


class PrevOrderForm(forms.Form):
    time_from = forms.DateTimeField(label='Time From', initial=datetime.now, required=True,
                                    input_formats=['%Y-%m-%dT%H:%M'],
                                    widget=widgets.DateTimeInput(
                                        format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}))
    time_to = forms.DateTimeField(label='Time To', initial=datetime.now, required=True,
                                  input_formats=['%Y-%m-%dT%H:%M'],
                                  widget=widgets.DateTimeInput(
                                      format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}))
    man_type = forms.BooleanField(label='Man', initial=True)
    man_type_quant = forms.IntegerField(label='Quantity', max_value=10, required=False)
    woman_type = forms.BooleanField(label='Woman', required=False)
    woman_type_quant = forms.IntegerField(label='Quantity', max_value=10, required=False)
    child_type = forms.BooleanField(label='Child', required=False)
    child_type_quant = forms.IntegerField(label='Quantity', max_value=10, required=False)
