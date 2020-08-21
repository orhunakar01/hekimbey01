# Generated by Django 3.0.8 on 2020-07-23 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0017_auto_20200723_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='form3',
            name='iptal',
            field=models.BooleanField(default=False, verbose_name='İşlemi İptal Et'),
        ),
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 23, 11, 35, 5, 473998, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]