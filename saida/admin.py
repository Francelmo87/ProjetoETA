from django.contrib import admin

from .models import Saida

# Register your models here.


@admin.register(Saida)
class EtaUmAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'cloro', 'cor_t', 'ph_t', 'turbidez_t',)


