# Generated by Django 3.0.8 on 2020-07-23 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0018_auto_20200723_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='iptal',
            field=models.BooleanField(default=False, verbose_name='Firma ile Anlaşılamadı'),
        ),
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 23, 11, 40, 50, 663947, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]
