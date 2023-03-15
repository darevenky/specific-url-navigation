from django.urls import path
from rcb.views import *

app_name='rcb'

urlpatterns=[
    path('dupli/',dupli,name='dupli'),
]