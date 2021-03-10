from django.shortcuts import render

# Create your views here.
'''
    Initial page just to init the demo
'''
def index(request):
    return render(request, 'index.html')