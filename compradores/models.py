# -*- coding: utf-8 -*-

from django.db import models
from userprofiles.models import UserProfile


class Comprador(models.Model):
    nombre = models.CharField("Nombre(s)", max_length=140)
    a_paterno = models.CharField("Apellido paterno", max_length=140)
    a_materno = models.CharField("Apellido materno", max_length=140)
    userprofile = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return "%s - %s - %s" % (self.a_paterno, self.a_materno, self.nombre)
        """
        return "%s  %s  %s %i" % (self.a_paterno, self.a_materno, self.nombre, self.id)
        """
