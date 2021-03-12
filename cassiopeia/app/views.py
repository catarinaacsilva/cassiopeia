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
    submitbutton= request.POST.get("submit")

    firstname = ''
    lastname = ''
    email = ''
    datein = ''
    dateout = ''
    
    form= ReceiptForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        email = form.cleaned_data.get('email')
        datein = form.cleaned_data.get('datein')
        dateout = form.cleaned_data.get('dateout')

    context= {'form': form, 'firstname': firstname, 'lastname':lastname, 'email':email, 'datein':datein, 'dateout':dateout,
              'submitbutton': submitbutton}
    
    Create_User.objects.create(email=email, firstname=firstname, lastname=lastname, datein=datein, dateout=dateout)

    return render(request, 'form.html', context)

'''
    Create policy and store it on database to reuse
'''

def addPolicy(request):
    submitbutton= request.POST.get("submit")

    policy = ''
    
    form= PolicyForm(request.POST or None)
    if form.is_valid():
        policy = form.cleaned_data.get('policy')

    context= {'form': form, 'policy': policy,
              'submitbutton': submitbutton}
    
    Create_Policy.objects.create(policy=policy)
    
    return render(request, 'request_consent.html', context)


'''
    Show a list with all the policies and provide a way to select one

    TODO: policy is none... it is not assign the value to the variable
'''
'''
def choosePolicy(request):
    submitbutton= request.POST.get("submit")

    policy = ''

    form = ListPolicies(request.POST or None)
    
    if form.is_valid():
        policy = form.cleaned_data.get('policy')
    print(policy)

    context= {'form': form, 'policy': policy,
              'submitbutton': submitbutton}
    
    return render(request, 'listPolices.html', context)
'''

