from django import forms
from bootstrap_datepicker.widgets import DatePicker
#from bootstrap_daterangepicker import widgets, fields


class ReceiptForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}))