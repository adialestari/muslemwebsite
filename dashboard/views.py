from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate, get_user
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import requests
from django.contrib.auth.hashers import make_password
from django.db import transaction
import random
import string
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def is_operator(user):
    if user.groups.filter(name="Operator").exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "back/dashboard.html" 
    
    if request.user.groups.filter(name="Operator").exists():
        request.session['is_operator'] = 'operator'
    
    users = User.objects.all();
    
    context ={
        "users" : users
    }
    
    return render(request, template_name, context)   

@login_required
def tableSholat(request):
    template_name = "back/tableSholat.html" 
    
    baca = SholatDoa.objects.filter(nama=request.user)
    
    context ={
        "read" : baca
    }
    
    return render(request, template_name, context)   

@login_required
def tableDoa(request):
    template_name = "back/tableDoa.html" 
    
    baca = DoaDoa.objects.filter(nama=request.user)
    
    context ={
        "read" : baca
    }
    
    return render(request, template_name, context)   


def loginPage(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    
    
    template_name = "back/loginPage.html" 
    
    
    
    if request.method == "POST":
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        
        user = authenticate(request, username=get_username, password=get_password)
        
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            print("username or password salah")
    
    return render(request, template_name)   

@login_required
@user_passes_test(is_operator)
def registerPage(request):
    template_name = "back/registerPage.html"
    
    if request.method == "POST" :
  
        username = request.POST.get('username')
        get_password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        
        User.objects.create(
            username = username,
            password = make_password(get_password),
            first_name = first_name,
            last_name = last_name,
            email = email,
        )
        return redirect(dashboard)
        
    
    return render(request, template_name)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required
def addBacaanSholat(request):
    template_name = "back/addBacaanSholat.html"
    
    if request.method == "POST":
        randkun = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        get_judul = request.POST.get('judul')
        get_konten = request.POST.get('konten1')
        users = request.user
        idcol = randkun
        
        SholatDoa.objects.create(
            nama = users,
            judul = get_judul,
            deskripsi = get_konten,
            idcol = idcol
        )
        
        return redirect(tableSholat)
    
    return render(request, template_name)

@login_required
def editSholat(request, id):
    
    template_name = "back/addBacaanSholat.html"
    cek2 = SholatDoa.objects.get(id=id)
    
    if request.method == "POST":
        randkun = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        get_judul = request.POST.get('judul')
        get_konten = request.POST.get('konten1')
        users = request.user
        idcol = randkun
        
        
        cek2.nama = users
        cek2.judul = get_judul
        cek2.deskripsi = get_konten
        cek2.idcol = idcol
        cek2.save()
        return redirect(tableSholat)
        
    
    context = {
        "cek" : cek2
    }
    
    return render(request, template_name, context)
    
@login_required
def addDoa(request):
    template_name = "back/addDoa.html"
    
    if request.method == "POST":
        randkun = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        get_judul = request.POST.get('judul')
        get_konten = request.POST.get('konten1')
        users = request.user
        idcol = randkun
        
        DoaDoa.objects.create(
            nama = users,
            judul = get_judul,
            deskripsi = get_konten,
            idcol = idcol
        )
        
        return redirect(tableDoa)
    
    return render(request, template_name)

@login_required
def editDoa(request, id):
    
    template_name = "back/addDoa.html"
    cek3 = DoaDoa.objects.get(id=id)
    
    
    if request.method == "POST":
        randkun = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        get_judul = request.POST.get('judul')
        get_konten = request.POST.get('konten1')
        users = request.user
        idcol = randkun
        
        
        cek3.nama = users
        cek3.judul = get_judul
        cek3.deskripsi = get_konten
        cek3.idcol = idcol
        cek3.save()
        return redirect(tableDoa)
        
    
    context = {
        "cek" : cek3
    }
    
    return render(request, template_name, context)

@login_required
def hapusSholat(request, id):
    SholatDoa.objects.get(id=id).delete()
    return redirect(tableSholat)

@login_required
def hapusDoa(request, id):
    DoaDoa.objects.get(id=id).delete()
    return redirect(tableDoa)
    
@login_required
def hapusUser(request, id):
    User.objects.get(id=id).delete()
    return redirect(dashboard)
    