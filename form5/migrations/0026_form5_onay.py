# Generated by Django 3.0.8 on 2020-08-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0025_auto_20200806_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='form5',
            name='onay',
            field=models.BooleanField(default=False, verbose_name='Ödeme Alındı'),
        ),
    ]
