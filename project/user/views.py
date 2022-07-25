from email import message
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from itertools import chain
import random
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home/')
        else:
            messages.info(request, 'User Invalid')
            return redirect('/login/')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['password_again']

        if password == password_again:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken :(")
                return redirect("redirect")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken :(")
                return redirect("redirect")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/login/')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


