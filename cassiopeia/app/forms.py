from django import forms
#from bootstrap_datepicker.widgets import DatePicker

from .models import Policy, Device, User

class UserForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    #datein = forms.DateField()
    #dateout = forms.DateField()

class StayForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StayForm, self).__init__(*args, **kwargs)
        # dynamic fields here ...
        qs = Device.objects.all()
        for r in qs:
            self.fields[f'device_{r.deviceid}'] = forms.ChoiceField(choices = (('Consent', True),('No consent', False)))
    # normal fields here ...
    email = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name="email", empty_label=None)
    datein = forms.DateField()
    dateout = forms.DateField()
    


class PolicyForm(forms.Form):
    policy = forms.CharField(max_length=1000)

class DeviceForm(forms.Form):
    device = forms.CharField(max_length=100)
    policyid = forms.ModelChoiceField(queryset=Policy.objects.all(), to_field_name="policyid", empty_label=None)
    
    #forms.CharField(max_length=100)

class ReceiptForm(forms.Form):
    version = forms.CharField(max_length=100)
    language = forms.CharField(max_length=100)
    selfservicepoint = forms.CharField(max_length=100)
    consent = forms.CharField(max_length=100)
    userid = forms.EmailField(max_length=100)
    privacyid = forms.CharField(max_length=100) # pode ser mais do que uma...
    device = forms.CharField(max_length=100) # pode ser mais do que um...
    entities = forms.CharField(max_length=100) # pode ser mais do que uma...
    otherinfo = forms.CharField(max_length=100)


'''
class ListPolicies(forms.Form):
    def listP():
        p = []
        qs = Create_Policy.objects.all()
        for r in qs:
            p.append((r.policyid,r.policy))

        return p
    
    policies = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=listP())
'''