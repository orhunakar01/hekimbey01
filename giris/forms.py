from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    kullanici_adi = forms.CharField(max_length=50, label='Kullanıcı Adı',required=True)
    sifre = forms.CharField(max_length=50, label='Parola', widget=forms.PasswordInput,required=True)




