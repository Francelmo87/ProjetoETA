from django.db import models


# Create your models here.
HORA_CHOICE = [
    ('0:00', '0:00'),
    ('2:00', '2:00'),
    ('4:00', '4:00'),
    ('6:00', '6:00'),
    ('8:00', '8:00'),
    ('10:00', '10:00'),
    ('12:00', '12:00'),
    ('14:00', '14:00'),
    ('16:00', '16:00'),
    ('18:00', '18:00'),
    ('20:00', '20:00'),
    ('22:00', '22:00'),
]


class Etatres(models.Model):
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

    class Meta:
        ordering = ('-data',)
        verbose_name = 'ETA TRÊS'

    def __str__(self):
        return self.hora

