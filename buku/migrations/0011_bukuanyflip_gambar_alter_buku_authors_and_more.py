# Generated by Django 4.1.7 on 2024-08-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0010_kategoribukuanyflip_lembaga_bukuanyflip'),
    ]

    operations = [
        migrations.AddField(
            model_name='bukuanyflip',
            name='gambar',
            field=models.FileField(blank=True, null=True, upload_to='bukuanyflip'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='authors',
            field=models.ManyToManyField(to='buku.author'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='kategoris',
            field=models.ManyToManyField(to='buku.kategori'),
        ),
    ]
