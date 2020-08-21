from django.contrib import admin

from .models import Form2


class form2Admin(admin.ModelAdmin):
    list_display = ['Olusturan', 'Sorumlusu', 'AtanmaTarihi', 'Aciklama']
    list_display_links = ['AtanmaTarihi']
    list_filter = ['Olusturan','Sorumlusu',"AtanmaTarihi","Aciklama"]
    search_fields = ['Olusturan', 'Sorumlusu', 'AtanmaTarihi', 'Aciklama']
    class Meta:
        model = Form2


admin.site.register(Form2, form2Admin)