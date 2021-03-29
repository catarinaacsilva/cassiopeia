import json
import logging
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.conf import settings
from .models import Create_User, Create_Policy


logger = logging.getLogger(__name__)

'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')

'''
    Receipt management
'''
def receiptManagement(request):
    return render(request, 'receiptManagement.html')

def formRegisterUser(request):
    return render(request, 'registerUser.html')


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
    datein = parameters['datein']
    dateout = parameters['dateout']

    try:
        Create_User.objects.create(email=email, firstname=firstname, lastname=lastname, datein=datein, dateout=dateout)
        url = settings.DATA_RETENTION_STAY
        user = {'datein':datein, 'dateout':dateout, 'email':email}
        x = requests.post(url, data=user)
    except:
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
        Create_Policy.objects.create(policy=policy)
    except:
        return Response('Cannot create the policy record', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)

'''
    Give consent to an input policy
'''
@csrf_exempt
@api_view(('POST',))
def giveConsent(request):
    parameters = json.loads(request.body)
    email = parameters['email']
    policyid = parameters['policyid']
    consent = parameters['consent']
    
    try:
        Consent_Reply.objects.create(email=email, policyid=policyid, consent=consent)
        #verificar se esta bem
        timestamp = Consent_Reply.objects.filter(policyid=policyid, email=email, consent=consent).order_by('timestamp')[0]
        url = settings.DATA_RETENTION_CONSENT
        policy = {'policyid':policyid, 'consent':consent, 'email':email, 'timestamp':timestamp}
        x = requests.post(url, data=policy)
    except:
        return Response('Cannot create the consent record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


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
    policyid = request.GET['policyid']
    email = request.GET['email']

    r = Consent_Reply.objects.filter(policyid=policyid, email=email).order_by('timestamp')[0]
    consent = r.consent

    version = 1

    url = settings.RECEIPT_URL
    x = requests.get(f'{url}/receipt?v={version}&')
    if x.status_code == 200:
        return JsonResponse(x.text)
    
    return Response('Problem', status=status.HTTP_400_BAD_REQUEST)


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