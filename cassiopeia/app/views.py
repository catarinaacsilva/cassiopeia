import logging
from django.shortcuts import render
#from .forms import ReceiptForm, PolicyForm, ListPolicies
from .forms import ReceiptForm, PolicyForm

from .models import Create_User, Create_Policy


logger = logging.getLogger(__name__)

'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')

'''
    Register temporary user in the system
'''

def registerUser(request):
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    datein = request.GET['datein']
    dateout = request.GET['dateout']

    Create_User.objects.create(email=email, firstname=firstname, lastname=lastname, datein=datein, dateout=dateout)

    return

'''
    Create policy and store it on database to reuse
'''
def addPolicy(request):
    policy = request.GET['policy']
    Create_Policy.objects.create(policy=policy)

    return

'''
    Give consent to an input policy and user
'''
def giveConsent(request):
    email = request.GET['email']
    policyid = request.GET['policyid']
    status = request.GET['status']

    if (Consent_Reply.objects.get(email=email) != None) and (Consent_Reply.objects.get(policyid=policyid) != None):
        Consent_Reply.objects.create(status=status)

    return 

'''
    The method has a JSON as input (parameter). This JSON has all the devices to integrate.
'''
def addDevices(request):
    