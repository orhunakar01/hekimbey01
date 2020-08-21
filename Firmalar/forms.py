from django import forms
from .models import Firmalar


class FirmalarForm(forms.ModelForm):


    class Meta:
        model = Firmalar
        fields = ['firma_adi', 'firma_adresi', 'firma_telefon']

