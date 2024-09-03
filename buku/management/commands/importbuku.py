from django.core.management.base import BaseCommand
import csv
import random
from django.db import transaction



from buku.models import *

class Command(BaseCommand):
    help = 'Import Buku dari CSV'    

    # @transaction.atomic
    def handle(self, *args, **kwargs):        
        with open('/home/btiums/Documents/Projects/django/jasmine/data/archive/books.csv') as file_obj:
            
            # Create reader object by passing the file 
            # object to reader method
            reader_obj = csv.reader(file_obj)
            
            # lewati header
            row1 = next(reader_obj)
            
            # Iterate over each row in the csv 
            # file using reader object
            counter = 0
            for row in reader_obj:
                try:        
                    # buat buku baru                                                        
                    buku = Buku.objects.create(
                        tahun = random.randint(1990, 2023),
                        judul = row[11],
                        sinopsis = row[2],
                        isbn = row[5],                        
                        format = row[1],                        
                        halaman = row[8],
                        cetakan_ke = 1,
                        stok = 10,
                        harga = random.randint(20000, 700000),
                        cover_url = row[4]                        
                    )

                    # buat author baru jika tidak ada
                    authors_data = row[0].split(',')                    
                    for author in authors_data:
                        if author == " ":
                            pass
                        author_obj = Author.objects.filter(nama=author)
                        if author_obj:                    
                            buku.authors.add(author_obj.first())
                        else:
                            author_new = Author.objects.create(nama=author)
                            buku.authors.add(author_new)                        

                    # buat kategori baru jika tidak ada
                    kategoris_data = row[3].split(',')
                    for kategori in kategoris_data:
                        if kategori == " ":
                            pass
                        kategori_obj = Kategori.objects.filter(nama=kategori)
                        if kategori_obj:                    
                            buku.kategoris.add(kategori_obj.first())
                        else:
                            kategori_new = Kategori.objects.create(nama=kategori)
                            buku.kategoris.add(kategori_new)                  

                    # counter
                    counter += 1                  
                    print(F"{counter} {buku}")

                except Exception as e:
                    print(e)
                