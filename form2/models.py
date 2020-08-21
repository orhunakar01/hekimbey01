from django.db import models
from django.contrib.auth import authenticate
from django.utils import timezone
from django.conf import settings
from django.db import models
from form_1.models import Form1
from django.contrib.auth.models import User
from collections import UserList


class Form2(models.Model):

    all_users = User.objects.all().order_by('username')
    all_user_choices = [(x.username , x.username) for x in all_users]

    Olusturan=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Form22 = models.ForeignKey(Form1 , on_delete=models.PROTECT , blank=True , null=True)
    Sorumlusu = models.CharField(choices=all_user_choices , max_length=25 , verbose_name='Sorumlu Kişiyi Ata' ,
                                 blank=False)
    AtanmaTarihi = models.DateTimeField(default=timezone.now, blank=False)
    Aciklama = models.TextField(verbose_name='Açıklama           ' , blank=False)



    def publish(self):
        self.AtanmaTarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.Sorumlusu
