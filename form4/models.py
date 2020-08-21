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
from form3.models import Form3

class Form4(models.Model):
    Olusturan = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)
    Form44=models.ForeignKey(Form3,on_delete=models.PROTECT,null=True,blank=True)
    onay=models.BooleanField(default=False,verbose_name='Firma adına yapacağımız hizmet tamamlandı mı?')
    aciklama=models.TextField(verbose_name='Açıklama                ',blank=True)
    tarih=models.DateTimeField(default=timezone.now, blank=False)

    def publish(self):
        self.tarih = timezone.now()
        self.save()

    def __str__(self):
        return self.aciklama