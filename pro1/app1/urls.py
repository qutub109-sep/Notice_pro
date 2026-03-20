from django.urls import path
from .views import *

urlpatterns=[
    path('',Home),
    path('Login',login),
    path('Dashboard',Dashboard),
    path('notice',notice),
    path('student',student),

]