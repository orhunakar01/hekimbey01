from django import forms

from form2.models import Form2
from .models import Form3
from form_1.models import Form1
from django.forms import ModelForm
from .models import Malzeme
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class Form3Form(forms.ModelForm):
    #isin_kategorisi=forms.ModelChoiceField(queryset=Form1.objects.get(Form1_id=Form1))
    class Meta:
        model = Form3
        fields = ['isin_kategorisi', 'Aciklama', 'tarih','dosya','iptal']
        widgets={
            'tarih': DatePickerInput(format='%d/%m/%Y') ,

        }

class MalzemeForm(forms.ModelForm):
    class Meta:
        model=Malzeme
        fields=['tarih','kimden','kime','sira_no','malzeme_adi','birim_fiyati','Miktari','olcu_birimi','tutar']

