from django.conf.urls import patterns, url
from .views import CasaGeneralCreateView, CreateFormCasaGeneralCasaMovimientoDef, UpdateFormCasaGeneralCasaMovimientoDef, CompradorGeneralMovimientoList

urlpatterns = patterns('',

     url(r'^casageneralcreate/(?P<slug>[\w\-]+)/(?P<pkslug>\d+)/$', CreateFormCasaGeneralCasaMovimientoDef, name='casageneralcreate'),
     url(r'^casageneralupdate/(?P<slug>[\w\-]+)/(?P<pkslug>\d+)/$', UpdateFormCasaGeneralCasaMovimientoDef, name='casageneralupdate'),
     url(r'^clientlistdetail/(?P<slug>[\w\-]+)/$', CompradorGeneralMovimientoList.as_view(), name='clientlistdetail'),
)
