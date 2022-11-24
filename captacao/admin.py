from django.contrib import admin

from .models import Captacao

# Register your models here.


@admin.register(Captacao)
class CaptacaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora',  'cor_b', 'ph_b', 'turbidez_b',)