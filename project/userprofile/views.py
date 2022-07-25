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

@login_required(login_url='/login/')
def profile(request):
    return render(request, "profile.html")