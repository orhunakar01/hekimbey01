# Generated by Django 3.0.8 on 2020-07-15 06:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0003_auto_20200714_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 6, 8, 19, 415155, tzinfo=utc)),
        ),
    ]