from django.db import models


# Create your models here.

class ReportIncidentModel(models.Model):

    location = models.CharField(max_length=50, blank=True)

    incident_department = models.TextField(max_length=300, blank=True)

    date = models.CharField(max_length=30, blank=True)

    time = models.CharField(max_length=30 , blank=True)

    incident_location = models.TextField(max_length=100, blank=True)

    initial_severity = models.CharField(max_length=30, blank=True)

    suspected_cause = models.TextField(max_length=100, blank=True)

    immediate_action_taken = models.TextField(max_length=100, blank=True)

    sub_incident_type = models.CharField(max_length=30, blank=True)

    reporting_user = models.CharField(max_length=50, blank=True)

    def __str__(self):

        return self.location
