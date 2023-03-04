from django.apps import AppConfig
from watson import search as watson_search


class BukuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buku'
    
    def ready(self):
        buku_model  = self.get_model("Buku")
        watson_search.register(buku_model)
