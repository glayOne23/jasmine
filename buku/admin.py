from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buku)
admin.site.register(Author)
admin.site.register(Kategori)
admin.site.register(KategoriBukuAnyFlip)
admin.site.register(Lembaga)
admin.site.register(BukuAnyFlip)


