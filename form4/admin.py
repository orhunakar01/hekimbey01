from django.contrib import admin

from .models import Form4


class form4Admin(admin.ModelAdmin):
    list_display = ['Olusturan', 'onay', 'tarih','aciklama']
    list_filter = ['Olusturan','onay',"aciklama","tarih"]
    search_fields = ['Olusturan', 'onay', 'tarih', 'aciklama']
    class Meta:
        model = Form4


admin.site.register(Form4, form4Admin)