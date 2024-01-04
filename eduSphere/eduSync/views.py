from django.shortcuts import render, redirect, HttpResponse
from eduSync.emailBackend import emailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def GENERIC(request):
    return render(request, 'generic.html')

def LOGIN(request):
    return render(request, 'login.html')

def signin(request):
    if request.method == "POST":
        user = emailBackend.authenticate(request, username = request.POST.get('email'),
                                         password = request.POST.get('password'))
        if user != None:
            login(request, user)
            userType = user.userType
            if userType == '1':
                return HttpResponse("This is Department Head Panel")
            elif userType == '2':
                return HttpResponse("This is Faculty Panel")
            elif userType == '3':
                return HttpResponse("This is Student Panel")
            else:
                # Message for login error
                messages.error(request, "Incorrect Credentials")
                return redirect('login')
        else:
                messages.error(request, "Incorrect Credentials")
                return redirect('login')
            



