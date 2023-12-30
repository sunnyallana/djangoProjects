from django.shortcuts import render, redirect

# Create your views here.
def generic(request):
    return render(request, 'generic.html')

def login(request):
    return render(request, 'login.html')