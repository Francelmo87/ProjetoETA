from django.contrib import admin

from .models import EtaUm

# Register your models here.


@admin.register(EtaUm)
class EtaUmAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'cloro', 'cor_d', 'ph_d', 'turbidez_d', 'cor_t', 'ph_t', 'turbidez_t',
                    'filtro1', 'filtro2', 'filtro3', 'filtro4',)
