# Generated by Django 3.0.8 on 2020-08-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0025_auto_20200727_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='isin_kategorisi',
            field=models.CharField(choices=[('Sağlık', 'Sağlık'), ('OSGB', 'OSGB'), ('Diğer', 'Diğer')], max_length=25),
        ),
    ]
