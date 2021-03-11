import logging
from django.shortcuts import render
from .forms import ReceiptForm, PolicyForm

from .models import Create_User

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
    date = ''
    
    form= ReceiptForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        email = form.cleaned_data.get('email')
        date = form.cleaned_data.get('date')

    context= {'form': form, 'firstname': firstname, 'lastname':lastname, 'email':email, 'date':date,
              'submitbutton': submitbutton}
    
    Create_User.objects.create(email, firstname, lastname, date)

    return render(request, 'form.html', context)

'''
    Create policy and store it on database to reuse
'''
def addPolicy(request):
    submitbutton= request.POST.get("submit")

    policy = ''
    
    form= PolicyForm(request.POST or None)
    if form.is_valid():
        policy = form.cleaned_data.get('firstname')

    context= {'form': form, 'policy': policy,
              'submitbutton': submitbutton}
    
    return render(request, 'request_consent.html', context)