from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def beranda(request):
  context = {}

  # ===[Fetch Data]===      

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)