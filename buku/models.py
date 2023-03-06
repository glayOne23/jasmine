from django.db import models


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
    authors = models.ManyToManyField(Author, blank=True, null=True)
    kategoris = models.ManyToManyField(Kategori, blank=True, null=True)
    cover_url = models.CharField(max_length=225, blank=True, null=True)
    cover = models.FileField(upload_to ='files/cover/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.judul} {self.tahun}"