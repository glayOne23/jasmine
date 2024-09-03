"""command buku anyflip"""
import csv

from buku.models import *
from django.core.files import File
from django.core.management.base import BaseCommand
from django.core.files import File as DjangoFile
from django.shortcuts import get_object_or_404


class Command(BaseCommand):
    """command buku anyflip"""
    help = 'Import Buku AnyFlip dari CSV'

    # @transaction.atomic
    def handle(self, *args, **kwargs):
        with open('static/anyflip/AnyFlip.csv', encoding="utf-8") as file_obj:
            reader_obj = csv.reader(file_obj, delimiter = ',')

            for row in reader_obj:
                kategori = get_object_or_404(KategoriBukuAnyFlip, nama=row[0].strip())
                lembaga = get_object_or_404(Lembaga, nama=row[1].strip())
                nama1, nama2 = kategori.nama.split(' AKADEMIK UNIVERSITAS MUHAMMADIYAH SURAKARTA TAHUN AKADEMIK ')
                nama = f"{nama1} {lembaga.nama} {nama2}"

                django_file = DjangoFile(
                    open(row[3], mode='rb'),
                    name=row[3].replace('static/anyflip/panduan_akademik/', '')
                )

                BukuAnyFlip.objects.update_or_create(
                    kategori=kategori,
                    lembaga=lembaga,
                    nama=nama,
                    defaults={
                        'url': row[2].strip(),
                        'gambar': django_file
                    }
                )
