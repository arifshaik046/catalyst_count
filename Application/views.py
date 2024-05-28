import time

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Application.models import UserProfile
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Passwords do not match.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists.")

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password1
        )
        user.save()

        messages.success(request, "You have successfully registered.")
        return redirect('/home/')
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
