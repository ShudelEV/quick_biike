from django import forms
from django.forms import widgets


class PrevOrderForm(forms.Form):
    time_from = forms.DateTimeField(label='Time From', required=True,
                                    widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    time_to = forms.DateTimeField(label='Time To', required=True,
                                  widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
