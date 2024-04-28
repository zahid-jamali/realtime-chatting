from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def home(request):
    obj=models.chat_rooms.objects.all()
    return render(request, "home.html", {'data':obj})

@login_required(login_url="login")
def chatFunc(request, pk):
    print(pk, " ", type(pk))
    rm=models.chat_rooms.objects.get(title=pk)
    if rm is None:
        return redirect("home")
    # rm=1
    obj=models.chattings.objects.filter(room=rm).order_by("-id")
    return render(request, "chat.html", {'data':obj, 'room':rm, 'user':request.user})

@login_required(login_url="login")
def logoutFunc(request):
    logout(request)
    return redirect("login")

def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    form=forms.CustomUserCreationFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, 'signin.html', {'form':form})

def loginFunction(request):
    if request.user.is_authenticated:
        return redirect("home")
    form=forms.loginForm(request.POST or None)
    if request.method == 'POST':
        uemail=request.POST.get("username")
        upass=request.POST.get("password")
        user=authenticate(request, email=uemail, password=upass)
        login(request, user)
    return render(request, 'login.html', {'form':form})