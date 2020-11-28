from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):

    email = forms.CharField(max_length=30)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta():

        model = User

        fields = ('first_name','last_name','email','username','password')
