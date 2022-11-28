# Generated by Django 4.1.3 on 2022-11-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EtaCinco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('hora', models.CharField(choices=[('1:00', '1:00'), ('3:00', '3:00'), ('5:00', '5:00'), ('7:00', '7:00'), ('9:00', '9:00'), ('11:00', '11:00'), ('13:00', '13:00'), ('15:00', '15:00'), ('17:00', '17:00'), ('19:00', '19:00'), ('21:00', '21:00'), ('23:00', '23:00')], max_length=5)),
                ('lavagem', models.BooleanField(blank=True, default=False, verbose_name='Lavagem')),
                ('cloro', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Cloro')),
                ('cor_t', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Cor Tratada')),
                ('ph_t', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ph Tratada')),
                ('turbidez_t', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Turbidez Tratada')),
            ],
            options={
                'verbose_name': 'ETA Cinco',
                'ordering': ('-data',),
            },
        ),
    ]