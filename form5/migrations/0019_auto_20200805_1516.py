# Generated by Django 3.0.8 on 2020-08-05 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0018_auto_20200805_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form5',
            name='faturaVade',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fatura Vadesi     '),
        ),
        migrations.AlterField(
            model_name='form5',
            name='odemePeriyodu',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ödeme Periyodu             '),
        ),
        migrations.AlterField(
            model_name='form5',
            name='periyotOdemeTutari',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='(Yaklaşık)Her bir periyottaki Alınacak Tutar           '),
        ),
        migrations.AlterField(
            model_name='form5',
            name='tarih',
            field=models.DateTimeField(blank=True, null=True, verbose_name=' Varsa Ödeme Periyodu Biteceği Tarih         '),
        ),
        migrations.AlterField(
            model_name='form5',
            name='toplamOdemeTutari',
            field=models.DecimalField(decimal_places=2, max_digits=50, verbose_name='Toplam Alınacak Tutar        '),
        ),
    ]