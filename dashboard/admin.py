from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(SholatDoa)


admin.site.register(DoaDoa)

class AdminSholat(admin.ModelAdmin):
    list_display = ["idsholat", "lokasi", "subuh","zuhur", "asar", "maghrib", "isya"]

admin.site.register(JadwalSholat, AdminSholat)