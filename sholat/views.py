from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from datetime import date
import random
from dashboard.models import *

def sinkron_sholat(request):
    URL = "https://api.myquran.com/v1/sholat/kota/semua"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    todays = date.today()
    year = todays.year
    month = todays.month
    day = todays.day
    
    for d in data:
        cek_solat = JadwalSholat.objects.filter(idsholat=d['id'])
        if cek_solat.exists():
            solat = cek_solat.first()
            solat.idsholat = d['id']
            solat.lokasi = d['lokasi']
            solat.save()
        else:
            JadwalSholat.objects.create(
                idsholat = d['id'],
                lokasi = d['lokasi']         
            )
    ambil_solat = JadwalSholat.objects.all()
    
    for ambil in ambil_solat:
        url_detil_solat = "https://api.myquran.com/v1/sholat/jadwal/{}/{}/{}/{}".format(ambil.idsholat,year, month,day)
        r = requests.get(url_detil_solat,ambil.idsholat) 
        data = r.json()['data']['jadwal']
        ambil.subuh = data['subuh']
        ambil.zuhur = data['dzuhur']
        ambil.asar = data['ashar']
        ambil.maghrib = data['maghrib']
        ambil.isya = data['isya']
        ambil.save()
    return HttpResponse("<h1>berhasil sinkron API solat</h1>")

def home(request):
    template_name = "front/home.html"
    todays = date.today()
    year = todays.year
    month = todays.month
    day = todays.day
    
    URL = "https://api.myquran.com/v1/sholat/jadwal/2310/{}/{}/{}".format(year, month,day)
    URL2 = "https://quran-api-id.vercel.app/random"
    
    r = requests.get(url = URL)
    
    data = r.json()
    a = requests.get(url = URL2)
    
    data2 = a.json()
    
    context ={
       
        "data" : data['data']['jadwal'],
        "dataAR" : data2['arab'],
        "dataID" :data2['translation']
    }
    
    return render(request, template_name, context)

def jadwalsolat(request):
    template_name= "front/jadwal.html"

    jadwal = JadwalSholat.objects.all()
    
    context = {
        "jadwal" : jadwal
    }
    
    return render(request, template_name, context)

def search_jadwal(request):
    
    template_name= "front/jadwalsearch.html"

    sol = request.POST.get('sola')
    
    jadwal = JadwalSholat.objects.filter(idsholat=sol)
    jadwal1 = JadwalSholat.objects.all()
    
    print(sol)
    context = {
        "data" : jadwal[0],
        "jadwal" : jadwal1,
    }
    
    return render(request, template_name, context)


def pray(request):
    template_name = "front/pray.html"
    
    read = SholatDoa.objects.all()
    
    context = {
        "baca" : read
    }
    
    return render(request, template_name, context)

def doa(request):
    template_name = "front/doa.html"
    
    read = DoaDoa.objects.all()
    
    context = {
        "baca" : read
    }
    
    return render(request, template_name, context)

def about(request):
    template_name = "front/about.html"
    
    return render(request, template_name)