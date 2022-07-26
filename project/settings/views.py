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
from userprofile.models import *
# Create your views here.


@login_required(login_url='/login/')
def settings(request):

    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        if request.FILES.get("profileimg") == None: 
            
            fullname = request.POST["fullName"]
            bio = request.POST["bio"]
            profileimg = user_profile.profileimg
            backgroundimg = user_profile.backgroundimg

            user_profile.fullName = fullname
            user_profile.bio = bio
            user_profile.profileimg = profileimg
            user_profile.backgroundimg = backgroundimg
            user_profile.save()


        if request.FILES.get("profileimg") != None:
    
            backgroundimg = request.FILES.get("backgroundimg")
            fullname = request.POST["fullName"]
            bio = request.POST["bio"]
            profileimg = request.FILES.get("profileimg")

            user_profile.fullName = fullname
            user_profile.bio = bio
            user_profile.profileimg = profileimg
            user_profile.backgroundimg = backgroundimg
            user_profile.save()
    
        return redirect("home")

    return render(request, "setting.html", {"user_profile" : user_profile})

