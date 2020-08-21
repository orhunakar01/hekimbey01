from django.contrib import admin

from .models import Form3


class form3Admin(admin.ModelAdmin):
    list_display = ['Olusturan', 'isin_kategorisi', 'Aciklama', 'dosya','tarih','iptal']
    list_display_links = ['tarih']
    list_filter = ['Olusturan','isin_kategorisi',"Aciklama","dosya",'tarih','iptal']
    search_fields = ['Olusturan', 'isin_kategorisi', 'Aciklama', 'dosya','tarih','iptal']
    class Meta:
        model = Form3


admin.site.register(Form3, form3Admin)