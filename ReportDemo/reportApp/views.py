from django.shortcuts import render
from reportApp.forms import UserRegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from reportApp.models import ReportIncidentModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from reportApp.forms import ReportIncidentModelForm

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

@login_required
def ReportIncident(request):

    report = ReportIncidentModelForm()
    if request.method == 'POST':

        report = ReportIncidentModelForm(data = request.POST)

        if report.is_valid():

            report.save()

            return Dashboard(request)
        else:
            return HttpResponse('Error!')


    return render(request,'reportApp/ReportIncident.html',{'report':report})
