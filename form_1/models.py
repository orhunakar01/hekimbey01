from datetime import date
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models , utils
from django.contrib.auth.models import User

from Firmalar.models import Firmalar


class Form1(models.Model):
    Birim = (
        ('Sağlık', 'Sağlık'),
        ('OSGB', 'OSGB'),
        ('Diğer', 'Diğer'),
    )

    kategori = (
        ('ihale', 'ihale'),
        ('teklif', 'Teklif'),
        ('Malz.Tedariği', 'Malz.Tedariği'),
        ('Diğer', 'Diğer'),
    )

    sorumlu = (
        ('cengiz bey', 'Cengiz Bey'),
        ('tekin bey', 'Tekin Bey'),
        ('ilhan bey', 'İlhan Bey'),
        ('mustafa bey', 'Mustafa Bey'),
        ('diğer', 'Diğer'),

    )

    adana=Firmalar.objects.all().order_by('firma_adi')
    adana_choices=[(x.firma_adi,x.firma_adi) for x in adana]


    Firmaid=models.ForeignKey(Firmalar,on_delete=models.PROTECT,blank=True,null=True)
    FirmaAdi=models.CharField(choices=adana_choices,max_length=60,verbose_name='Firma Adı',blank=False)
    Olusturan=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    ilgili_birim = models.CharField(choices=Birim, max_length=25, verbose_name='İlgili Birim        ', blank=False)
    isin_kategorisi = models.CharField(choices=kategori, max_length=25, verbose_name='Yapılan İşin Kategorisi       ',blank=False)
    konusu = models.TextField(verbose_name='Konu ile ilgili Açıklama         ', blank=False)
    dosya = models.FileField( db_index=True,blank=True)
    sorumlu_kisi = models.CharField(choices=sorumlu, max_length=25, verbose_name='İşten Sorumlu Kişi        ', blank=False)
    baslangic = models.DateTimeField(default=timezone.now, blank=False)
    bitis = models.DateTimeField(default=date.today,blank=False)
    iptal=models.BooleanField(default=False,verbose_name='İşlemin Tamamını İptal Et')
    bugun = models.DateField(default=date.today)

    def publish(self):
        self.bitis = date.today()
        self.save()


