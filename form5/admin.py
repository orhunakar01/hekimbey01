from django.contrib import admin

from .models import Form5


class form5Admin(admin.ModelAdmin):
    list_display = ['Olusturan', 'odemePeriyodu','faturaVade', 'periyotOdemeTutari','toplamOdemeTutari','Aciklama','tarih','dosya']
    list_filter = ['Olusturan','odemePeriyodu','faturaVade',"periyotOdemeTutari","toplamOdemeTutari",'Aciklama','tarih','dosya']
    search_fields = ['Olusturan', 'odemePeriyodu', 'faturaVade','periyotOdemeTutari', 'toplamOdemeTutari','Aciklama','tarih','dosya']
    class Meta:
        model = Form5


admin.site.register(Form5, form5Admin)
