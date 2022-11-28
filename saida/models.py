from django.db import models


# Create your models here.
HORA_CHOICE = [
    ('1:00', '1:00'),
    ('3:00', '3:00'),
    ('5:00', '5:00'),
    ('7:00', '7:00'),
    ('9:00', '9:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('15:00', '15:00'),
    ('17:00', '17:00'),
    ('19:00', '19:00'),
    ('21:00', '21:00'),
    ('23:00', '23:00'),
]


class Saida(models.Model):
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    hora = models.CharField(max_length=5, choices=HORA_CHOICE)
    cloro = models.DecimalField('Cloro', max_digits=4, decimal_places=2, blank=True, null=True)
    fluor = models.DecimalField('Fluor', max_digits=4, decimal_places=2, blank=True, null=True)
    cor_t = models.DecimalField('Cor Bruta', max_digits=5, decimal_places=2, blank=True, null=True)
    ph_t = models.DecimalField('Ph Bruta', max_digits=5, decimal_places=2, blank=True, null=True)
    turbidez_t = models.DecimalField('Turbidez Bruta', max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ('-data',)
        verbose_name = 'CAPTAÇÃO'
        verbose_name_plural = 'CAPTAÇÕES'

    def __str__(self):
        return self.hora
