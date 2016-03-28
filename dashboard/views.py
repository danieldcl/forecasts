from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def tables(request):
    return render(request, 'dashboard/tables.html')

def login(request):
    return render(request, 'dashboard/login.html')

def morris(request):
    return render(request, 'dashboard/morris.html')

def flot(request):
    return render(request, 'dashboard/flot.html')

def forms(request):
    return render(request, 'dashboard/forms.html')
