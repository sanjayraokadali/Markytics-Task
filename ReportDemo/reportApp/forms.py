from django.contrib.auth.models import User
from django import forms
from reportApp.models import ReportIncidentModel

class UserRegistrationForm(forms.ModelForm):

    email = forms.CharField(max_length=30)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta():

        model = User

        fields = ('first_name','last_name','email','username','password')

class ReportIncidentModelForm(forms.ModelForm):

    LOCATION_CHOICES = [
    ('London','London'),
    ('Edinburgh','Edinburgh'),
    ('Glasgow','Glasgow')

    ]

    location = forms.CharField(label = 'Location' , widget = forms.Select(choices=LOCATION_CHOICES))

    SEVERITY = [

    ('Mild','Mild'),
    ('Moderate','Moderate'),
    ('Severe','Severe'),
    ('Fatal','Fatal'),


    ]

    initial_severity = forms.CharField(label = 'Initial Severity', widget = forms.Select(choices=SEVERITY))

    INCIDENT_TYPE = [
    ('Environmental Incident','Environmental Incident'),
    ('Injury/Illness','Injury/Illness'),
    ('Property Damage','Property Damage'),
    ('Vehicle','Vehicle')

    ]

    sub_incident_type = forms.MultipleChoiceField(required=True, widget = forms.CheckboxSelectMultiple, choices = INCIDENT_TYPE )

    class Meta():

        model = ReportIncidentModel

        fields = ('location','incident_department','date_time','incident_location','initial_severity','suspected_cause',
                   'immediate_action_taken','sub_incident_type')
