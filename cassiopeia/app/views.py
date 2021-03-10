from django.shortcuts import render

from .forms import ReceiptForm


'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')

def registerUser(request):
    submitbutton= request.POST.get("submit")

    firstname=''
    lastname=''

    form= ReceiptForm(request.POST or None)
    if form.is_valid():
        firstname= form.cleaned_data.get("firstname")
        lastname= form.cleaned_data.get("lastname")


    context= {'form': form, 'firstname': firstname, 'lastname':lastname,
              'submitbutton': submitbutton}

    return render(request, 'form.html', context)