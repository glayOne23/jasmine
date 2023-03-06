# Generated by Django 4.1.7 on 2023-03-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0005_alter_buku_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, to='buku.author'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='kategoris',
            field=models.ManyToManyField(blank=True, null=True, to='buku.kategori'),
        ),
    ]