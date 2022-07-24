from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate
# Create your views here.

def register(request):
    """ Register a new user """
    if (request.method == "POST"):
        firstname, lastname, username = request.POST['firstname'], request.POST['lastname'], request.POST['username']
        contact, email = request.POST['contact'], request.POST['email']
        password, repeated_password = request.POST['password'], request.POST['repeatpassword']

        if firstname is None:
            messages.info(request, "Enter first name")
            return redirect("register")

        if password == repeated_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists!')
                return redirect("register")
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists!')
                return redirect("register")
            if CustomUser.objects.filter(contact=contact).exists():
                messages.info(request, 'Contact Already Exists!')
                return redirect("register")

            new_user = CustomUser.objects.create_user(
                first_name=firstname,
                last_name =lastname,
                username=username,
                contact=contact,
                email=email,
                password=password
            )
            return redirect("login")
        else:
            messages.info(request, "Passwords are not the same!")
            return redirect("register")

    elif (request.method == "GET"):
        return render(request, 'register.html')

def login(request):
    """ Log in a user """
    
    if (request.method == "POST"):
        username, password = request.POST['username'], request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(user)
                return redirect("/")
        return HttpResponse("sorry")
    else:
        return render(request, 'login.html')