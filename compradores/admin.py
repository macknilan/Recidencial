# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Comprador
from actions import export_as_excel


class CompradorAdmin(admin.ModelAdmin):
    list_display = ('userprofile', 'nombre', 'a_paterno', 'a_materno',)
    list_filter = ('userprofile', )
    search_fields = ('nombre', 'a_paterno', 'a_materno', )
    actions = (export_as_excel, )


admin.site.register(Comprador, CompradorAdmin)
