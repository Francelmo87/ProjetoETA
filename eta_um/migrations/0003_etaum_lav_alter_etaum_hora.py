# Generated by Django 4.1.3 on 2022-11-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eta_um', '0002_rename_eta1_etaum'),
    ]

    operations = [
        migrations.AddField(
            model_name='etaum',
            name='lav',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='etaum',
            name='hora',
            field=models.CharField(choices=[('1:00', '1:00'), ('3:00', '3:00'), ('5:00', '5:00'), ('7:00', '7:00'), ('9:00', '9:00'), ('11:00', '11:00'), ('13:00', '13:00'), ('15:00', '15:00'), ('17:00', '17:00'), ('19:00', '19:00'), ('21:00', '21:00'), ('23:00', '23:00')], max_length=5),
        ),
    ]
