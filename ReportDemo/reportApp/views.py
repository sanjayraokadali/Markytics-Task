from django.shortcuts import render
from reportApp.forms import UserRegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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

    return render(request,'reportApp/Register.html',{'form':form})



    return render(request,'reportApp/Register.html')

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

            return render(request,'reportApp/Login.html',{'message':'User Not Found! Please Login'})

    return render(request,'reportApp/Login.html',{'user':username})

def Dashboard(request):

    return render(request,'reportApp/Dashboard.html')

@login_required
def Logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('basepage'))
