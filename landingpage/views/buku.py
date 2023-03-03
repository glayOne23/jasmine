from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone


def index(request):
  context = {}

  # ===[Fetch Data]===      
  context['books'] = range(4)

  # ===[Render Template]===
  context['page'] = 'buku.index'
  return render(request, 'landingpage/buku/index.html', context)