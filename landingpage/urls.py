from django.urls import path, include
from django.contrib.auth.decorators import login_required

from landingpage.views import (
    landingpage,
    buku
)

app_name= 'landingpage'

urlpatterns = [
    path('', landingpage.beranda, name='beranda'),    
    path('buku/', include([        
        path('', buku.index, name='buku'),
        # path('create/', buku.SetReviewerView.as_view(), name='buku.create'),
        # path('<int:id>/update/', buku.SetReviewerView.as_view(), name='buku.update'),
        path('<int:id>/', buku.show, name='buku'),
        path('<int:id>/baca_pdf', buku.baca_pdf, name='buku.baca_pdf'),
    ])),            
]

