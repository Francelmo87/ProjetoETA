from django.contrib import admin

from .models import EtaQuatro

# Register your models here.


@admin.register(EtaQuatro)
class EtaUmAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'cloro', 'lavagem', 'cor_t', 'ph_t', 'turbidez_t',
                    'filtro2', 'filtro3', 'filtro5', 'filtro6', 'filtro7')

