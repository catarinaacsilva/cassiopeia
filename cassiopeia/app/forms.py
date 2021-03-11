from django import forms
#from bootstrap_datepicker.widgets import DatePicker

from .models import Create_Policy

class ReceiptForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    date = forms.DateField()

class PolicyForm(forms.Form):
    policy = forms.CharField(max_length=1000)
    name = forms.CharField(max_length=100)

class ListPolicies(forms.Form):
    def listP():
        p = []
        qs = Create_Policy.objects.all()
        for r in qs:
            p.append((r.policyid,r.policy))

        return p
    
    policies = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=listP())
