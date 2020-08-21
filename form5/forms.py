from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Form5
from form_1.models import Form1
from django.forms import ModelForm


class Form5Form(forms.ModelForm):
    class Meta:
        model = Form5
        fields = ['odemePeriyodu', 'periyotOdemeTutari', 'toplamOdemeTutari','Aciklama','tarih','faturaVade','dosya',"onay"]
        widgets={
            'faturaVade':DatePickerInput(format='%d/%m/%Y'),
            'tarih':DatePickerInput(format='%d/%m/%Y'),
        }

