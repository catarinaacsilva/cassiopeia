import logging
from django.shortcuts import render
from .forms import ReceiptForm

logger = logging.getLogger(__name__)

'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')

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

    return render(request, 'form.html', context)