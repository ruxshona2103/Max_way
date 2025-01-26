

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    # faculties = services.get_faculties()
    # kafedras = services.get_kafedra()
    # subjects = services.get_subject()
    # teachers = services.get_teacher()
    # groups = services.get_groups()
    # students = services.get_student()
    ctx={
        'counts' : {
            'faculties':len(faculties),
            'kafedras':len(kafedras),
            'subjects':len(subjects),
            'teachers':len(teachers),
            'groups':len(groups),
            'students':len(students)
        }
    }
    return render(request, 'index.html', ctx)

