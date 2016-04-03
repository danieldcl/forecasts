from django.shortcuts import render
from general_functions import generate_prediction

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

def results(request):
    data=''
    if request.POST and request.FILES:
        fi = request.FILES['csv_file']
        attr = request.POST['attr']
        mod = request.POST['predicting_model']
        data = generate_prediction(fi, mod, attr)
        fi.close()
    return render(request, "dashboard/results.html", {'data':data})
