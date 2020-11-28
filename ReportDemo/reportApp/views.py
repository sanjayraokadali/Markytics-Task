from django.shortcuts import render

# Create your views here.
def BasePage(request):

    return render(request,'reportApp/BasePage.html')

def Register(request):

    return render(request,'reportApp/Register.html')

def Login(request):

    return render(request,'reportApp/Login.html')

def Dashboard(request):

    return render(request,'reportApp/Dashboard.html')
