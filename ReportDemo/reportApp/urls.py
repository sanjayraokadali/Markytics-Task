from django.conf.urls import url
from reportApp import views

app_name = 'reportApp'

urlpatterns = [

    url('^$',views.Dashboard,name='dashboard'),
    url('^Register/$',views.Register,name='register'),
    url('^Login/ReportIncident/$',views.ReportIncident,name='reportincident'),

]
