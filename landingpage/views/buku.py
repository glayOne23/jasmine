from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.paginator import Paginator


from buku import repositories as repo


def index(request):  
  context = {}

  # ===[Fetch Data]===      
  bukus_data = repo.buku.all_revert()  
  kategoris_data = repo.kategori.limit(13)
  context['kategoris'] = [
    {
      'id': kategori.id,
      'nama': kategori.nama,
      'jumlah': kategori.buku_set.all().count()
    }
    for kategori in kategoris_data
  ]

  # ===[Fetch Paginator]===      
  page_number = request.GET.get('page', 1)
  paginator = Paginator(bukus_data, 21)
  context['bukus'] = paginator.get_page(page_number)

  # ===[Render Template]===
  context['page'] = 'buku'
  return render(request, 'landingpage/buku/index.html', context)


def show(request, id):  
  context = {}

  # ===[Fetch Data]===      
  context['buku'] = repo.buku.get(id)
  kategoris_data = repo.kategori.limit(13)
  context['kategoris'] = [
    {
      'id': kategori.id,
      'nama': kategori.nama,
      'jumlah': kategori.buku_set.all().count()
    }
    for kategori in kategoris_data
  ]  


  # ===[Render Template]===
  context['page'] = 'buku'
  return render(request, 'landingpage/buku/show.html', context)