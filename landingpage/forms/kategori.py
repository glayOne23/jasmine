from django import forms
from buku.models import Kategori


class KategoriCheckboxForm(forms.Form):
    kategori = forms.ModelMultipleChoiceField(
        queryset=Kategori.objects.all(), widget=forms.CheckboxSelectMultiple()
    )
