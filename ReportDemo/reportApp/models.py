from django.db import models


# Create your models here.

class ReportIncidentModel(models.Model):

    location = models.CharField(max_length=50)

    incident_department = models.TextField(max_length=300)

    date = models.CharField(max_length=30)

    time = models.CharField(max_length=30)

    incident_location = models.TextField(max_length=100)

    initial_severity = models.CharField(max_length=30)

    suspected_cause = models.TextField(max_length=100)

    immediate_action_taken = models.TextField(max_length=100)

    sub_incident_type = models.CharField(max_length=30)

    def __str__(self):

        return self.location
