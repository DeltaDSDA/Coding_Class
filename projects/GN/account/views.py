from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth

def login_view(request):
    return render(request, 'account/login.html')

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'account/users.html', {'users': users})
