# Generated by Django 3.0.8 on 2020-08-06 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0024_auto_20200806_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form5',
            name='faturaVade',
            field=models.DateField(default=datetime.date.today, verbose_name='Fatura Vadesi'),
        ),
    ]