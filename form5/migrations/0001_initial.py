# Generated by Django 3.0.8 on 2020-07-24 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form4', '0009_auto_20200724_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odemePeriyodu', models.DecimalField(blank=1, decimal_places=2, max_digits=50, verbose_name='Ödeme Periyodu')),
                ('periyotOdemeTutari', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='(Yaklaşık)Her bir periyottaki Alınacak Tutar')),
                ('toplamOdemeTutari', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='Toplam Alınacak Tutar ')),
                ('Aciklama', models.TextField(verbose_name='Açıklama Giriniz')),
                ('dosya', models.FileField(blank=True, db_index=True, upload_to='')),
                ('tarih', models.DateField(blank=True, verbose_name=' Varsa Ödeme Periyodu Biteceği Tarih')),
                ('faturaVade', models.DateField(default=django.utils.timezone.now, verbose_name='Fatura Vadesi')),
                ('Form55', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='form4.Form4')),
                ('Olusturan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
