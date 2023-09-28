from django.contrib.auth import logout,authenticate, login as auth_login  
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'core/login.html')

def iniciar_sesion (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  
            return redirect('/admin/')
        else:
            messages.error(request, "Nombre o contraseña incorrectos, ingrese nuevamente")

    return render(request, 'core/login.html')

