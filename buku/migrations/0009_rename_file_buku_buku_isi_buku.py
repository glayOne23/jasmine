# Generated by Django 4.1.7 on 2023-03-06 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0008_buku_file_buku'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='file_buku',
            new_name='isi_buku',
        ),
    ]