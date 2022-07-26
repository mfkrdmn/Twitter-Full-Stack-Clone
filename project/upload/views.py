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

@login_required(login_url='signin')
def upload(request):

    if request.method == "POST":
        
        user = request.user.username
        image = request.FILES.get("image_upload")
        caption = request.POST["caption"]
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/profile/'+user)

    else:
        return redirect("/")