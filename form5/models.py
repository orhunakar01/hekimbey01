from django.db import models
from django.contrib.auth import authenticate
from django.utils import timezone
from django.conf import settings
from django.db import models
from form_1.models import Form1
from form2.models import Form2
from django.contrib.auth.models import User
from collections import UserList
from django.db import models
from form4.models import Form4
from datetime import date , datetime


class Form5(models.Model):
    Olusturan = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)
    Form55 = models.ForeignKey(Form4 , on_delete=models.PROTECT , null=True , blank=True)
    # Bu alana malzeme tedarik .html gibi formların goruntulenmesi gelecek.
    # Konu ne ile ilgili ise;
    odemePeriyodu = models.PositiveIntegerField(verbose_name='Ödeme Periyodu             ' , blank=True,null=True)
    periyotOdemeTutari = models.DecimalField(verbose_name='(Yaklaşık)Her bir periyottaki Alınacak Tutar           ' , blank=True ,
                                             null=True,max_digits=50,decimal_places=2)
    toplamOdemeTutari = models.DecimalField(verbose_name='Toplam Alınacak Tutar        ' , blank=False,max_digits=50,decimal_places=2)
    Aciklama = models.TextField(verbose_name='Açıklama Giriniz' , blank=False)
    tarih = models.DateTimeField(verbose_name=' Varsa Ödeme Periyodu Biteceği Tarih         ' , blank=True,null=True)
    faturaVade = models.DateField(default=date.today, blank=False , verbose_name='Fatura Vadesi')
    bugun=models.DateField(default=date.today)
    dosya = models.FileField(db_index=True , blank=False , verbose_name='Fatura PDF Ekleyiniz.',upload_to='files/')
    onay = models.BooleanField(default=False , verbose_name='Ödeme Alındı')

    def publish(self):
        self.faturaVade = date.today()
        self.save()


    def __str__(self):
        return self.Olusturan
