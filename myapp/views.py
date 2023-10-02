from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import ClientForm
from .models import Client

user = User

# Create your views here.
def signup(request):
    username = request.POST.get('nome')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    email = request.POST.get('email')

    if password == password2:
        user = User(username=username,password=make_password(password),email=email)
        user.save()
        return HttpResponse(f'Usuário {username} Cadastrado')
    else:
        return HttpResponse(f'Senhas não batem')

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    
    elif request.method == 'POST':
        global user
        user = authenticate(request=request,username=request.POST.get('nome'),password=request.POST.get('password'))
        if user:
            login(request=request,user=user)
            return redirect("./")
        else:
            return render(request,'login.html')

@login_required(login_url='/signin')
def home(request):
    global user
    context = {}
    form = ClientForm()
    last_login = user.last_login

    context = {
        'last_access':last_login,
        'username':user.username,
        'form':form
    }
    
    return render(request,'home.html',context=context)

def logout_from_home(request):
    logout(request)
    return render(request,'login.html')

def register(request):
    
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    sexual_orientation = request.POST.get('sexual_orientation')
    interest = request.POST.get('interest')
    photo = request.POST.get('photo')

    client = Client(age=age,gender=gender,sexual_orientation=sexual_orientation,interest=interest,photo=photo)
    client.save()
    
    return HttpResponse(request)