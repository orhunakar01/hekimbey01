# Generated by Django 3.0.8 on 2020-07-16 05:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0007_auto_20200715_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 5, 36, 26, 821378, tzinfo=utc)),
        ),
    ]
