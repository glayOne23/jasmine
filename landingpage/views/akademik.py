from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from buku.models import Lembaga, KategoriBukuAnyFlip, BukuAnyFlip


def index(request):
    context = {}

    # ===[Fetch Data]===
    context['kategoris'] = KategoriBukuAnyFlip.objects.filter(nama="BUKU PANDUAN AKADEMIK UNIVERSITAS MUHAMMADIYAH SURAKARTA TAHUN AKADEMIK 2024/2025").order_by('-id')

    # ===[Render Template]===
    context['page'] = 'pedoman-akademik'
    return render(request, 'landingpage/pedoman_akademik/index.html', context)


def show(request, id):
    context = {}

    # ===[Fetch Data]===
    context['buku'] = get_object_or_404(BukuAnyFlip, id=id)

    # ===[Render Template]===
    context['page'] = 'pedoman-akademik'
    return render(request, 'landingpage/pedoman_akademik/show.html', context)
