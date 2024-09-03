""""""
from django.db import models


KELOMPOK_PEMBACA = [
    (1, 'Anak'),
    (2, 'Dewasa'),
    (3, 'Semua Umur'),
]

JENIS_PUSTAKA = [
    (1, 'Fiksi'),
    (2, 'Non Fiksi'),
]

KATEGORI_JENIS = [
    (1, 'Terjemahan'),
    (2, 'Non Terjemahan'),
]

KATEGORI_BUKU = [
    (1, 'Lepas'),
    (2, 'Berjilid'),
]



class Author(models.Model):
    nama = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nama}"


class Kategori(models.Model):
    nama = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nama}"


class Buku(models.Model):
    tahun = models.IntegerField()
    judul = models.TextField(blank=True, null=True)
    sinopsis = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=225, blank=True, null=True)
    dimensi = models.CharField(max_length=225, blank=True, null=True)
    format = models.CharField(max_length=225, blank=True, null=True)
    halaman = models.CharField(max_length=225, blank=True, null=True)
    cetakan_ke = models.IntegerField(blank=True, null=True)
    stok = models.IntegerField(blank=True, null=True)
    harga = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    kategoris = models.ManyToManyField(Kategori)
    cover_url = models.CharField(max_length=225, blank=True, null=True)
    cover = models.FileField(upload_to ='files/cover/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # baru
    kelompok_pembaca = models.IntegerField(null=True, choices=KELOMPOK_PEMBACA)
    jenis_pustaka = models.IntegerField(null=True, choices=JENIS_PUSTAKA)
    kategori_jenis = models.IntegerField(null=True, choices=KATEGORI_JENIS)
    kategori_buku = models.IntegerField(null=True, choices=KATEGORI_BUKU)
    isi_buku = models.FileField(upload_to ='files/isibuku/', blank=True, null=True)

    def __str__(self):
        return F"{self.judul} {self.tahun}"


class Lembaga(models.Model):
    nama = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nama}"


class KategoriBukuAnyFlip(models.Model):
    nama = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nama}"


class BukuAnyFlip(models.Model):
    kategori = models.ForeignKey(KategoriBukuAnyFlip, on_delete=models.CASCADE)
    lembaga = models.ForeignKey(Lembaga, on_delete=models.CASCADE)
    nama = models.CharField(max_length=225)
    url = models.URLField()
    gambar = models.FileField(upload_to='bukuanyflip', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nama}"
