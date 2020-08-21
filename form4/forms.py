from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Form3
from form_1.models import Form1
from django.forms import ModelForm
from .models import Form4


class Form4Form(forms.ModelForm):

    class Meta:
        model = Form4
        fields = ['onay', 'aciklama', 'tarih']
        widgets={
            'tarih':DatePickerInput(format='%d/%m/%Y'),
        }