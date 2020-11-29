from django.shortcuts import render
from reportApp.forms import UserRegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from reportApp.models import ReportIncidentModel

# Create your views here.
def BasePage(request):

    return render(request,'reportApp/BasePage.html')

def Register(request):

    form = UserRegistrationForm()

    if request.method == 'POST':

        form = UserRegistrationForm(data = request.POST)

        if form.is_valid():

            user = form.save()

            user.set_password(user.password)

            user.save()

            return Dashboard(request)
        else:
            return HttpResponse('Please Try Again!')

    return render(request,'reportApp/Register.html',{'form':form})


def Login(request):

    username= ''

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username = username, password=password)

        if user:

            login(request,user)

            return HttpResponseRedirect(reverse('reportApp:dashboard'))
        else:

            return render(request,'reportApp/Login.html',{'message':'Invalid details! Please Try again...'})

    return render(request,'reportApp/Login.html',{'user':username})

def Dashboard(request):

    return render(request,'reportApp/Dashboard.html')

@login_required
def Logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('basepage'))


def ReportIncident(request):

    if request.method =='POST':

        location = request.POST.get('location')
        incident_department = request.POST.get('incident_department')
        date = request.POST.get('date')
        time = request.POST.get('time')
        incident_location = request.POST.get('incident_location')
        initial_severity = request.POST.get('initial_severity')
        suspected_cause = request.POST.get('suspected_cause')
        immediate_action = request.POST.get('immediate_action')

        environmental_incident = request.POST.get('environmental_incident')
        injury = request.POST.get('injury')
        property_damaged = request.POST.get('property_damaged')
        vehicle = request.POST.get('vehicle')

        report = ReportIncidentModel.objects.create(location = location, incident_department = incident_department,
        date = date, time = time, incident_location = incident_location, initial_severity = initial_severity,
        suspected_cause = suspected_cause, immediate_action_taken = immediate_action, sub_incident_type = [environmental_incident,injury,property_damaged,vehicle]
        )

        report.save()

        return Dashboard(request)


    return render(request,'reportApp/ReportIncident.html')
