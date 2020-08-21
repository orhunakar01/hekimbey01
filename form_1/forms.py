from django import forms

from Firmalar.models import Firmalar
from .models import Form1
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class Form1Form(forms.ModelForm):

    class Meta:
        model=Form1
        fields=[
            'FirmaAdi',
            'ilgili_birim',
            'isin_kategorisi',
            'konusu',
            'dosya',
            'sorumlu_kisi',
            'baslangic',
            'bitis',
            'iptal'
        ]
        widgets = {
            'baslangic': DatePickerInput(format='%d/%m/%Y'),
            'bitis': DatePickerInput(format='%d/%m/%Y',options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale":"tr"
                }),
        }

