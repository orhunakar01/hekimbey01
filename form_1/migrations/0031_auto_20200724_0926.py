# Generated by Django 3.0.8 on 2020-07-24 06:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0030_auto_20200723_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 6, 26, 13, 897785, tzinfo=utc)),
        ),
    ]
