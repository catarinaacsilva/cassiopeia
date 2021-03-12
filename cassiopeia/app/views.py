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

def registerUser(request):
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    datein = request.GET['datein']
    dateout = request.GET['dateout']

    Create_User.objects.create(email=email, firstname=firstname, lastname=lastname, datein=datein, dateout=dateout)

    pass

'''
    Create policy and store it on the database to reuse
'''
def addPolicy(request):
    policy = request.GET['policy']
    Create_Policy.objects.create(policy=policy)

    pass

'''
    Give consent to an input policy and user
'''
@csrf_exempt
@api_view(('POST',))
def giveConsent(request):
    parameters = json.loads(request.body)
    print(parameters)
    email = parameters['email']
    policyid = parameters['policyid']
    consent = parameters['consent']
    
    #try:
        #Consent_Reply.objects.create(email=email, policyid=policyid, consent=consent)
    #except:
        #return Response('Cannot create the consent record', status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


'''
    The method has a JSON as input (parameter). This JSON has all the devices to integrate.
'''
def addDevices(request):
    pass




'''
    try:
        emaildb = Consent_Reply.objects.get(email=email)
        policydb = Consent_Reply.objects.get(policyid=policyid)
    except ObjectDoesNotExist:
        logger.erro('Object does not exist')
        return Response('Object does not exist', status=status.HTTP_400_BAD_REQUEST)
'''