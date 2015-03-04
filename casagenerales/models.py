# -*- coding: utf-8 -*-


from django.db import models
from compradores.models import Comprador


class CasaGeneral(models.Model):
    MANZANA = (
        (0, 'Cero'),
        (1, 'Uno'),
        (2, 'Dos'),
        (3, 'Tres'),
        (4, 'Cuatro'),
        (5, 'Cinco'),
        (6, 'Seis'),
        (7, 'Siete'),
        (8, 'Ocho'),
        (9, 'Nueve'),
        (10, 'Diez'),
    )
    LOTE = (
        (0, 'Cero'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
    )
    ETAPA = (
        ('selec_et', 'Selecciona etapa'),
        ('etapa_1_40',  'ETAPA 1 (40)'),
    )
    STATUS = (
        ('selec_sts', 'Selecciona status'),
        ('apartada', 'Apartada'),
        ('pagada', 'Pagada'),
    )
    manzana = models.IntegerField(
        "Manzana", max_length=2, choices=MANZANA, default=0)
    lote = models.IntegerField("Lote", max_length=1, choices=LOTE, default=0)
    etapa = models.CharField(
        "Etapa", max_length=15, choices=ETAPA, default='selec_et')
    status = models.CharField(
        "Status", max_length=10, choices=STATUS, default='selec_sts')
    comprador = models.OneToOneField(Comprador)

    def __unicode__(self):
        return str("%i - %i %s" %
                   (self.manzana, self.lote, self.status)
                   )
        # return self.comprador
        # return "%i" % (self.cliente)
