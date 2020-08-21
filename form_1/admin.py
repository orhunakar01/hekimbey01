from django.contrib import admin

from .models import Form1


class form1Admin(admin.ModelAdmin):
    list_display = ['ilgili_birim', 'isin_kategorisi', 'sorumlu_kisi', 'baslangic', 'bitis']
    list_display_links = ['bitis']
    list_filter = ['baslangic','bitis']
    search_fields = ['ilgili_birim', 'isin_kategorisi', 'sorumlu_kisi', 'baslangic', 'bitis','Olusturan','konusu']
    class Meta:
        model = Form1


admin.site.register(Form1, form1Admin)

# Register your models here.
