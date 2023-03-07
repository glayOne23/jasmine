from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.paginator import Paginator


from buku import repositories as repo


def index(request):  
  context = {}

  # ===[GET Search]===      
  search_text = request.GET.get('search', '')
  context['search_text'] = search_text
  search_kategori = request.GET.getlist('kategori')
  context['search_kategori'] = search_kategori

  # ===[Fetch Data]===      
  # by text
  if search_text: 
    bukus_data = repo.buku.search(search_text)
  else: 
    bukus_data = repo.buku.all_revert()  
  # by kategori
  if search_kategori:
    bukus_data = bukus_data.filter(kategoris__id__in=search_kategori)
    
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
  per_page = 21
  page_number = request.GET.get('page', 1)
  paginator = Paginator(bukus_data, per_page)
  bukus = paginator.get_page(page_number)
  context['bukus'] = bukus  
  dari = bukus.number if bukus.number == 1 else ((bukus.number-1) * per_page) + 1
  context['tampilkan'] = {
    'from': dari,
    'to': bukus.object_list.count() if bukus.number == 1 else dari + bukus.object_list.count() - 1,
    'total': bukus_data.count()
  }

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


def baca_pdf(request, id):
  context = {}

  # ===[Fetch Data]===      
  buku = repo.buku.get(id)  

  # ===[content]===    
  with open(buku.isi_buku.path, 'rb') as pdf:
      response = HttpResponse(pdf.read(), content_type='application/pdf')
      response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
      return response