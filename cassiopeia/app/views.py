import json
import logging
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.conf import settings
from .models import User, Policy, Device, Stay
from .forms import PolicyForm, DeviceForm, UserForm, StayForm, ReceiptForm


logger = logging.getLogger(__name__)


''' ##########################################################################
        INTERFACE
##########################################################################'''

'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')


'''
    Render the HTML to show the form to register user
'''
def formRegisterUser(request):
    form = UserForm()
    return render(request, 'registerUser.html', {'form': form})

'''
    Render the HTML to show the form to register stay
'''
def formRegisterStay(request):
    form = StayForm()
    return render(request, 'registerStay.html', {'form': form})

'''
    Render the HTML to show the form to add policy
'''
def formAddPolicy(request):
    form = PolicyForm()
    return render(request, 'addPolicy.html', {'form': form})


'''
    Render the HTML to show the form to add device
'''
def formAddDevice(request):
    form = DeviceForm()
    return render(request, 'addDevice.html', {'form': form})

'''
    Render the HTML to show the receipt request
'''
def formAddPolicy(request):
    form = ReceiptForm()
    return render(request, 'requestReceipt.html', {'form': form})


'''
    List all policies
'''
def listPolicies(request):
    policies = []
    
    policy_object = Policy.objects.all()
    for p in policy_object:
        di = {'id': p.policyid, 'policy': p.policy}

        policies.append(di)
        
    return render(request, 'listPolicies.html', {'Policies': policies})


'''
    List all devices
'''
def listDevices(request):
    devices = []
    
    device_object = Device.objects.all()
    for d in device_object:
        di = {'id': d.deviceid, 'name': d.device, 'policy': d.policyid}

        devices.append(di)
        
    return render(request, 'listDevices.html', {'Devices': devices})


'''
    List all users
'''
def listUsers(request):
    users = []
    
    user_object = User.objects.all()
    for u in user_object:
        di = {'email': u.email, 'FirstName': u.firstname, 'LastName': u.lastname}

        users.append(di)
        
    return render(request, 'listUsers.html', {'Users': users})


'''
    Ask for the consent and give it
'''
def formGiveConsent(request):
    return render(request, 'giveConsent.html')

'''
    Request Receipt
'''
def requestReceipt(request):
    return render(request, 'requestReceipt.html')


''' ##########################################################################
        API
##########################################################################  '''
'''
    Register temporary user in the system and post data on data retention
'''
@csrf_exempt
@api_view(('POST',))
def registerUser(request):
    parameters = json.loads(request.body)
    firstname = parameters['firstname']
    lastname = parameters['lastname']
    email = parameters['email']
    #datein = parameters['datein']
    #dateout = parameters['dateout']

    try:
        User.objects.create(email=email, firstname=firstname, lastname=lastname)
        #url = settings.DATA_RETENTION_STAY
        #user = {'datein':datein, 'dateout':dateout, 'email':email}
        #x = requests.post(url, data=user)
    except:
        return Response('Cannot create the user record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(('POST',))
def registerStay(request):
    parameters = json.loads(request.body)
    datein = parameters['datein']
    dateout = parameters['dateout']

    try:
        Stay.objects.create(datein=datein, dateout=dateout)
        #url = settings.DATA_RETENTION_STAY
        #user = {'datein':datein, 'dateout':dateout, 'email':email}
        #x = requests.post(url, data=user)
    except Exception as e:
        print(e)
        return Response('Cannot create the user record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


'''
    Create policy and store it on the database to reuse
'''
@csrf_exempt
@api_view(('POST',))
def addPolicy(request):
    parameters = json.loads(request.body)
    policy = parameters['policy']
    
    try:
        Policy.objects.create(policy=policy)
    except:
        return Response('Cannot create the policy record', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)


'''
    Add the available devices
'''
@csrf_exempt
@api_view(('POST',))
def addDevice(request):
    print(f'Add Device into DB')
    parameters = json.loads(request.body)
    print(parameters)
    device = parameters['device']
    policyid = parameters['policyid']
    
    try:
        policy = Policy.objects.get(policyid=policyid)
        Device.objects.create(device=device, policyid=policy)
    except Exception as e:
        print(e)
        return Response('Cannot create the device record', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)


'''
    Give consent to an input policy

@csrf_exempt
@api_view(('POST',))
def giveConsent(request):
    parameters = json.loads(request.body)
    email = parameters['email']
    policyid = parameters['policyid']
    consent = parameters['consent']
    
    try:
        Consent.objects.create(email=email, policyid=policyid, consent=consent)
        #verificar se esta bem
        timestamp = Consent.objects.filter(policyid=policyid, email=email, consent=consent).order_by('timestamp')[0]
        url = settings.DATA_RETENTION_CONSENT
        policy = {'policyid':policyid, 'consent':consent, 'email':email, 'timestamp':timestamp}
        x = requests.post(url, data=policy)
    except:
        return Response('Cannot create the consent record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)
'''

'''
    The method receives a list of devices (id or name) and store it on the database
'''
@csrf_exempt
@api_view(('POST',))
def addDevices(request):
    parameters = json.loads(request.body)
    email = parameters['email']
    policyid = parameters['policyid']

    try:
        for d in parameters['devices']:
            Device_Create.objects.create(device=d, email=email, policyid=policyid)
    except:
        return Response('Cannot create the device record', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)

'''
    Request a receipt
    TODO also send the signature
'''
@csrf_exempt
@api_view(('GET',))
def request_receipt(request):
    parameters = json.loads(request.body)
    version = parameters['version']
    organization = parameters['organization']
    selfservicepoint = parameters['selfservicepoint']
    userid = parameters[''] 
    privacyid = parameters['']
    device = parameters['']
    entities = parameters['']
    otherinfo = parameters['']

    try:
        url = settings.RECEIPTGENERATION
        r = {'datein':datein, 'dateout':dateout, 'email':email}
        x = requests.post(url, data=r)
    except:
        return Response('Cannot create the user record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


'''
    Receipt a receipt signed by the client

@csrf_exempt
@api_view(('POST', 'GET'))
def request_sig_receipt(request):
    parameters = json.loads(request.body)
    receipt = parameters['receipt']
    cert = parameters['cert']

    try:
        #validate signature and send to the receipt_generator
        
    except:
        return Response('Signature not valid', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)
'''