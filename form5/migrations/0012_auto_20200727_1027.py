# Generated by Django 3.0.8 on 2020-07-27 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0011_auto_20200727_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form5',
            name='bugun',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]