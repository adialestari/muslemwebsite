
from django.contrib import admin
from django.urls import path, include
from .views import *
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("pray/", pray, name="pray"),
    path("doa/", doa, name="doa"),
    path("about/", about, name="about"),
    path("jadwal/", jadwalsolat, name="jadwal"),
    path("search_jadwal/", search_jadwal, name="searchjadwal"),
    path("loginPage/", loginPage, name="loginpage"),
    path("logout/", logoutPage, name="logout"),
    path("sinkron_api/", sinkron_sholat, name="sinkron_sholat"),

    # app connection
    path("dashboard/", include("dashboard.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)