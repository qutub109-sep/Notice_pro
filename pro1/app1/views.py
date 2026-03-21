from django.shortcuts import render
from .models import *

# Create your views here.

def Home(req):
    return render(req,'Home.html')

def login(req):
    return render(req,'Login.html')

def Dashboard(req):
    return render(req,'Dashboard.html')

def notice1(req):
    if req.method=='POST':
        n_title=req.POST['ti']
        date=req.POST['ed']
        dis=req.POST['ds']
        pdf = req.FILES.get('notes')
        ob=Notice(title=n_title,expiry_date=date,description=dis, notice_pdf=pdf)
        ob.save()
        return render(req,'home.html')

    else:
        return render(req,'notice.html')

def student(req):
    return render(req,'student.html')

def Register(req):
    if req.method=='POST':
        name=req.POST['fn']
        email=req.POST['em']
        cour=req.POST['cs']
        passw=req.POST['pw']
        passw1=req.POST['pw1']
        ob=registers(full_name=name,email=email,course=cour,password=passw)

        ob.save()
        return render(req,'home.html')
    else:

         return render(req,'Register.html')