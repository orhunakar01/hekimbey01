# Generated by Django 3.0.8 on 2020-07-15 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0004_auto_20200715_0908'),
        ('form2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form2',
            name='Form2',
        ),
        migrations.AddField(
            model_name='form2',
            name='Form22',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='form_1.Form1'),
        ),
    ]
