from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("tablesholat/", tableSholat, name="tablesholat"),
    path("tabledoa/", tableDoa, name="tabledoa"),
    path("bacaanSholat/", addBacaanSholat, name="bacaansholat"),
    path("doa/", addDoa, name="adddoa"),
    path("editSholat/<int:id>", editSholat, name="editsholat"),
    path("editDoa/<int:id>", editDoa, name="editdoa"),
    path("hapusSholat/<int:id>", hapusSholat, name="hapussholat"),
    path("hapusDoa/<int:id>", hapusDoa, name="hapusdoa"),
    path("registerPage/", registerPage, name="registerpage"),
    path("hapusUser/<int:id>", hapusUser, name="hapusUser"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)