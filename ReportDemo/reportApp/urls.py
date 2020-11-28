from django.conf.urls import url
from reportApp import views

app_name = 'reportApp'

urlpatterns = [

    url('^$',views.Dashboard,name='dashboard'),
    url('^Login/$',views.Login,name='login'),
    url('^Register/$',views.Register,name='register'),

]
