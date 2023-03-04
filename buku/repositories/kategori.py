from buku.models import Kategori


class KategoriRepository:
    model = Kategori

    def all(self):        
        return self.model.objects.all()
    
    def limit(self, limit=10):        
        return self.model.objects.all()[:limit]


kategori = KategoriRepository()