# Generated by Django 3.0.8 on 2020-08-05 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0022_auto_20200805_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form5',
            name='faturaVade',
            field=models.DateField(default=datetime.date.today, verbose_name='Fatura Vadesi'),
        ),
    ]