from django.urls import path, include
from django.contrib.auth.decorators import login_required

from landingpage.views import (
    landingpage,
    buku
)

app_name= 'landingpage'

urlpatterns = [
    path('', landingpage.beranda, name='beranda'),
    path('buku/', buku.index, name='buku.index'),
]

