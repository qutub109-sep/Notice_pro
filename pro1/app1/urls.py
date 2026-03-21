from django.urls import path
from .views import *

urlpatterns=[
    path('',Home),
    path('index',Home),
    path('Login',login),
    path('Dashboard',Dashboard),
    path('notice',notice1),
    path('student',student),
    path('register',Register),

]