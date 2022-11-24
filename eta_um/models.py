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


class EtaUm(models.Model):
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    hora = models.CharField(max_length=5, choices=HORA_CHOICE)
    lavagem = models.BooleanField('Lavagem', default=False, blank=True)
    cloro = models.DecimalField('Cloro', max_digits=4, decimal_places=2, blank=True, null=True)
    cor_d = models.DecimalField('Cor Decantada', max_digits=4, decimal_places=2, blank=True, null=True)
    ph_d = models.DecimalField('Ph Decantada', max_digits=4, decimal_places=2, blank=True, null=True)
    turbidez_d = models.DecimalField('Turbidez Decantada', max_digits=4, decimal_places=2, blank=True, null=True)
    cor_t = models.DecimalField('Cor Tratada', max_digits=4, decimal_places=2, blank=True, null=True)
    ph_t = models.DecimalField('Ph Tratada', max_digits=4, decimal_places=2, blank=True, null=True)
    turbidez_t = models.DecimalField('Turbidez Tratada', max_digits=4, decimal_places=2, blank=True, null=True)
    filtro1 = models.DecimalField('Filtro 1', max_digits=4, decimal_places=2, blank=True, null=True)
    filtro2 = models.DecimalField('Filtro 2', max_digits=4, decimal_places=2, blank=True, null=True)
    filtro3 = models.DecimalField('Filtro 3', max_digits=4, decimal_places=2, blank=True, null=True)
    filtro4 = models.DecimalField('Filtro 4', max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'ETA 1'
        verbose_name_plural = 'ETAS 1'

    def __str__(self):
        return self.hora
