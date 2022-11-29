from django.contrib import admin

from .models import EtaTres

# Register your models here.


@admin.register(EtaTres)
class EtaUmAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'cloro', 'cor_d', 'ph_d', 'turbidez_d', 'cor_t', 'ph_t', 'turbidez_t',)

