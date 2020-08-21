from datetime import date
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models , utils
from django.contrib.auth.models import User



class Firmalar(models.Model):
    firma_adi=models.CharField(max_length=75,verbose_name='Firma Adı')
    firma_adresi=models.CharField(max_length=100,verbose_name='Adres')
    firma_telefon=models.CharField(max_length=30,verbose_name='Telefon Numarası')
    #form1 = models.OneToOneField(Form1 , on_delete=models.CASCADE,null=True,blank=True)
    #form2 = models.OneToOneField(Form2 , on_delete=models.CASCADE,null=True,blank=True)
    #form3 = models.OneToOneField(Form3 , on_delete=models.CASCADE,null=True,blank=True)
    #form4 = models.OneToOneField(Form4 , on_delete=models.CASCADE,null=True,blank=True)
    #form5 = models.OneToOneField(Form5 , on_delete=models.CASCADE,null=True,blank=True)
    #anasayfa=models.OneToOneField(Anasayfa,on_delete=models.CASCADE,null=True,blank=True)
    #Olusturan = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)

    def __str__(self):
        return self.firma_adi


