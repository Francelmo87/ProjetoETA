from django.contrib import admin

from .models import EtaCinco

# Register your models here.


@admin.register(EtaCinco)
class EtaUmAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'cloro', 'lavagem', 'cor_t', 'ph_t', 'turbidez_t',)

