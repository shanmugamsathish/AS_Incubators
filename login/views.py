from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def login(request):   
    return render(request,'login/login.html')
  
    
