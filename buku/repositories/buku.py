from buku.models import Kategori, Buku
from watson import search as watson


class BukuRepository:
    model = Buku

    def get(self, id):        
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            print(F"buku {id} tidak ada")

    def all_revert(self):        
        return self.model.objects.all().order_by('-id')
    
    def limit_revert(self, limit :int =10):        
        return self.model.objects.all().order_by('-id')[:limit]
    
    # def by_kategori_revert(self, kategori):
    #     return self.models.filter(kategoris__in = kategori).order_by('-id')

    def search(self, text):        
        return watson.filter(self.model, text)


buku = BukuRepository()