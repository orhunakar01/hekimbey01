# Generated by Django 3.0.8 on 2020-08-12 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0036_auto_20200808_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='bugun',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='form1',
            name='bitis',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]