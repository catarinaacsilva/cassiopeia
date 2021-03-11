from django import forms
from bootstrap_datepicker.widgets import DatePicker


class ReceiptForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    date = forms.DateField()