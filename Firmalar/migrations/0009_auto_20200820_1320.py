# Generated by Django 3.0.8 on 2020-08-20 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Firmalar', '0008_remove_firmalar_olusturan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmalar',
            name='firma_adi',
            field=models.CharField(default=datetime.datetime(2020, 8, 20, 10, 19, 55, 63017, tzinfo=utc), max_length=75, verbose_name='Firma Adı'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='firma_adresi',
            field=models.CharField(default=datetime.datetime(2020, 8, 20, 10, 20, 0, 879015, tzinfo=utc), max_length=100, verbose_name='Adres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='firma_telefon',
            field=models.CharField(default=datetime.datetime(2020, 8, 20, 10, 20, 5, 347016, tzinfo=utc), max_length=30, verbose_name='Telefon Numarası'),
            preserve_default=False,
        ),
    ]