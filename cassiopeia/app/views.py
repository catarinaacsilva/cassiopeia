import json
import logging
import requests
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.conf import settings
from .models import User, Policy, Device, Stay, Entity, Consent_Entity, Consent_Device, Receipt, Stay_Receipt
from .forms import PolicyForm, DeviceForm, UserForm, StayForm, EntityForm 




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
    Render the HTML to show the form to add entity
'''
def formAddEntity(request):
    form = EntityForm()
    return render(request, 'addEntity.html', {'form': form})


'''
    Render the HTML to show the receipt request
'''
def formReceiptRequest(request):
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
    List all entity
'''
def listEntities(request):
    entities = []
    
    entity_object = Entity.objects.all()
    for d in entity_object:
        di = {'id': d.entityid, 'name': d.entity, 'policy': d.policyid}

        entities.append(di)
        
    return render(request, 'listEntities.html', {'Entities': entities})


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
    List temporary receipts - receipts to sign
'''
def listReceipts(request):
    receipts = []
    
    receipt_object = Receipt.objects.all()
    for r in receipt_object:
        ri = {
            'receipt': json.dumps(r.json_receipt), 
            'timestampStored': r.timestamp_stored, 
            'timestampCreated': r.timestamp_created,
            'stayId': r.stayid,
            'pk': r.id
            }
        receipts.append(ri)
        
    return render(request, 'listReceipts.html', {'Receipts': receipts}) 



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
    print(parameters)
    datein = parameters['datein']
    dateout = parameters['dateout']
    email = parameters['email']
    device_pk = [x[7:] for x in parameters.keys() if x.startswith('device_')]
    entity_pk = [x[7:] for x in parameters.keys() if x.startswith('entity_')]


    version = 1
    language = 'EN'
    selfservicepoint = 'cassiopeia.id'
    userid = email
    devices = []
    entities = []
    otherinfo = ''

    try:
        #Create stay info in db
        user = User.objects.get(email=email)
        stay = Stay.objects.create(datein=datein, dateout=dateout, email=user)
        for pk in device_pk:
            device = Device.objects.get(deviceid = pk)
            consent_d = parameters[f'device_{pk}'] == 'True'
            Consent_Device.objects.create(stayid=stay, deviceid=device, consent=consent_d)
            devices.append({'ID': pk, 'Policy': device.policyid.pk, 'Consent': consent_d})
        
        for pk in entity_pk:
            entity = Entity.objects.get(entityid = pk)
            consent_e = parameters[f'entity_{pk}'] == 'True'
            Consent_Entity.objects.create(stayid=stay, entityid=entity, consent=consent_e)
            entities.append({'ID': pk, 'Policy': entity.policyid.pk, 'Consent': consent_e})
    

        url = settings.RECEIPTGENERATION
        r = {
            'version':version, 
            'language':language, 
            'selfservicepoint':selfservicepoint,
            'userid':userid,
            #'privacyid':privacyid,
            'devices':devices,
            'entities':entities,
            'otherinfo':otherinfo}
        x = requests.get(url, json=r)

        result = json.loads(x.text)

        receipt = result['receipt']
        timestamp = result['timestamp']

        dt_object = datetime.fromtimestamp(timestamp)

        Receipt.objects.create(timestamp_created=dt_object, json_receipt=receipt, stayid=stay)

        #url = settings.DATA_RETENTION_STAY
        #user = {'datein':datein, 'dateout':dateout, 'email':email}
        #x = requests.post(url, data=user)

    except Exception as e:
        print(e)
        return Response('Cannot create the stay record', status=status.HTTP_400_BAD_REQUEST)

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
    Add the available entities
'''
@csrf_exempt
@api_view(('POST',))
def addEntity(request):
    print(f'Add Entity into DB')
    parameters = json.loads(request.body)
    print(parameters)
    entity = parameters['entity']
    policyid = parameters['policyid']
    
    try:
        policy = Policy.objects.get(policyid=policyid)
        Entity.objects.create(entity=entity, policyid=policy)
    except Exception as e:
        print(e)
        return Response('Cannot create the entity record', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_201_CREATED)



'''
    Receive a signed receipt
'''
@csrf_exempt
@api_view(('POST',))
def signReceipt(request):
    parameters = json.loads(request.body)
    print(parameters)
    idreceipt = parameters['id']
    receipt = parameters['receipt']

    try:
        stayid = Receipt.objects.get(id=idreceipt).stayid

        url = settings.RECEIPTSTORE
        r = {
            'json_receipt':receipt, 
            'email': receipt['userid']
            }
        x = requests.post(url, json=r)

        if x.status_code != 200:
            raise Exception('RM failed')

        result = json.loads(x.text)
        print(result)
        
        # Delete temporary receipt
        Receipt.objects.filter(id=idreceipt).delete()

        # Store receipt reference
        Stay_Receipt.objects.create(stayid=stayid, receiptid=result['id_receipt'])

    except Exception as e:
        print(e)
        return Response('ERROR', status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)





