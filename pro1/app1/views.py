from django.shortcuts import render

# Create your views here.

def Home(req):
    return render(req,'Home.html')

def login(req):
    return render(req,'Login.html')

def Dashboard(req):
    return render(req,'Dashboard.html')

def notice(req):
    return render(req,'notice.html')

def student(req):
    return render(req,'student.html')