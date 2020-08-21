# Generated by Django 3.0.8 on 2020-08-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firmalar', '0002_auto_20200818_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmalar',
            name='firma_adi',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Firma Adı'),
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='firma_adresi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='firma_telefon',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefon Numarası'),
        ),
    ]
