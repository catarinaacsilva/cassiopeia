import json
import logging
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
    Give consent to an input policy and user
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
    try:
        emaildb = Consent_Reply.objects.get(email=email)
        policydb = Consent_Reply.objects.get(policyid=policyid)
    except ObjectDoesNotExist:
        logger.erro('Object does not exist')
        return Response('Object does not exist', status=status.HTTP_400_BAD_REQUEST)
'''