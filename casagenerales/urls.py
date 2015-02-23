from django.conf.urls import patterns, url
from .views import CasaGeneralCreateView, CreateFormCasaGeneralCasaMovimientoDef

urlpatterns = patterns('',

     url(r'^casageneralcreate/(?P<slug>[\w\-]+)/(?P<pkslug>\d+)/$', CreateFormCasaGeneralCasaMovimientoDef, name='casageneralcreate'),
#    url(r'^userupdate/(?P<slug>[\w\-]+)/$', UserUpdateView.as_view(), name='userupdate'),
#    url(r'^userprofileupdate/(?P<slug>[\w\-]+)/$', UserProfileUpdateView.as_view(), name='userprofileupdate'),
#    url(r'^userprofiledetail/(?P<slug>[\w\-]+)/$', UserProfileDetailView.as_view(), name='userprofiledetail'),
)
