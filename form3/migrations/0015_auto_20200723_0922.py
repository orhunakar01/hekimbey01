# Generated by Django 3.0.8 on 2020-07-23 06:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0014_auto_20200722_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 23, 6, 22, 57, 83573, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]