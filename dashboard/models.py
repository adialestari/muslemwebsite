from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SholatDoa(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    idcol = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class Meta:
        verbose_name_plural = 'Bacaan Sholat'

class DoaDoa(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    idcol = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class Meta:
        verbose_name_plural = 'Doa'
        
class JadwalSholat(models.Model):
    idsholat = models.CharField(max_length=225, blank=True, null=True)
    lokasi = models.CharField(max_length=225, blank=True, null=True)
    subuh = models.CharField(max_length=225, blank=True, null=True)
    zuhur = models.CharField(max_length=225, blank=True, null=True)
    asar = models.CharField(max_length=225, blank=True, null=True)
    maghrib = models.CharField(max_length=225, blank=True, null=True)
    isya = models.CharField(max_length=225, blank=True, null=True)