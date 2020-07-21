# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse
from .models import Profile


def signup(request):
   if request.method == "POST":
       username = request.POST["username"]
       password = request.POST["password1"]
       major = request.POST["major"]
       ordinal = request.POST["ordinal"]

       user = User.objects.create_user(username=username, password=password)
       user.profile.major = major
       user.profile.ordinal = ordinal
       user.save()

       login_user = django_authenticate(username=username, password=password)
       django_login(request, login_user)
       return JsonResponse({"response": "signup success"})

