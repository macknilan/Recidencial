# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import CasaGeneral
from actions import export_as_excel


@admin.register(CasaGeneral)
class CasaGeneralAdmin(admin.ModelAdmin):
    list_display = ('comprador', 'manzana', 'lote', 'etapa', 'status', )
    list_filter = ('comprador', 'manzana', 'lote', 'etapa', 'status', )
    search_fields = ('comprador__nombre', 'comprador__a_paterno', 'comprador__a_materno', 'manzana', 'lote', 'etapa', 'status', )
    actions = (export_as_excel, )
    raw_id_fields = ('comprador', )


# admin.site.register(CasaGeneral, CasaGeneralAdmin)
