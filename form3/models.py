import json
from datetime import datetime , date

from django.db import models
from django.contrib.auth import authenticate
from django.utils import timezone
from django.conf import settings
from django.db import models
from form_1.models import Form1
from form2.models import Form2
from django.contrib.auth.models import User
from collections import UserList


class Form3(models.Model):
    Olusturan = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)



    isin_kategorisi = models.CharField(choices=Form1.kategori,max_length=25,blank=False)
    Form33=models.ForeignKey(Form2,on_delete=models.PROTECT , blank=True , null=True)
    Aciklama = models.TextField(verbose_name='Açıklama', blank=True)
    dosya = models.FileField(db_index=True , blank=True)
    tarih=models.DateField(default=timezone.now, blank=False)
    iptal = models.BooleanField(default=False , verbose_name='Firma ile Anlaşılamadı')

    def publish(self):
        self.tarih = timezone.now()
        self.save()

    def __str__(self):
        return self.isin_kategorisi

class Malzeme(models.Model):
    sira_no= models.CharField(max_length=30,blank=True)
    malzeme_adi=models.CharField(max_length=30,blank=True)
    birim_fiyati=models.CharField(max_length=30,blank=True)
    Miktari=models.CharField(max_length=30,blank=True)
    olcu_birimi=models.CharField(max_length=30,blank=True)
    tutar=models.CharField(max_length=30,blank=True)
    Form333=models.ForeignKey(Form3,on_delete=models.CASCADE)
    tarih=models.CharField(max_length=30,blank=True)
    kimden=models.CharField(max_length=30,blank=True)
    kime=models.CharField(max_length=30,blank=True)


    def set_sira_no(self, x):
        self.sira_no = json.dumps(x)

    def get_sira_no(self):
        return json.loads(self.sira_no)


    def set_malzeme_adi(self, x):
        self.malzeme_adi = json.dumps(x)

    def get_malzeme_adi(self):
        return json.loads(self.malzeme_adi)



    def set_birim_fiyati(self, x):
        self.birim_fiyati = json.dumps(x)

    def get_birim_fiyati(self):
        return json.loads(self.birim_fiyati)



    def set_Miktari(self, x):
        self.Miktari = json.dumps(x)

    def get_Miktari(self):
        return json.loads(self.Miktari)



    def set_olcu_birimi(self, x):
        self.olcu_birimi = json.dumps(x)

    def get_olcu_birimi(self):
        return json.loads(self.olcu_birimi)


    def set_tutar(self, x):
        self.tutar = json.dumps(x)

    def get_tutar(self):
        return json.loads(self.tutar)



