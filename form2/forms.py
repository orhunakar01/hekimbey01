from django import forms
from .models import Form2
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class Form2Form(forms.ModelForm):


    class Meta:
        model = Form2
        fields = ['Sorumlusu',
                  'Aciklama',
                  'AtanmaTarihi'
                  ]
        widgets = {
            'AtanmaTarihi': DatePickerInput(format='%d/%m/%Y'),
        }
