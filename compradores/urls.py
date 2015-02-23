from django.conf.urls import patterns, url

from .views import CompradorCreateDef, CompradorListView, CompradorUpdateView

urlpatterns = patterns('',

     url(r'^compradorcreate/(?P<slug>[\w\-]+)/$', CompradorCreateDef, name='compradorcreate'),
     url(r'^clienteslist/(?P<asesor>[\w\-]+)/$', CompradorListView.as_view(), name='clienteslist'),
     url(r'^clienteupdate/(?P<slug>[\w\-]+)/(?P<pk>\d+)/$', CompradorUpdateView.as_view(), name='clienteupdate'),
#    url(r'^userupdate/(?P<slug>[\w\-]+)/$', UserUpdateView.as_view(), name='userupdate'),
#    url(r'^userprofileupdate/(?P<slug>[\w\-]+)/$', UserProfileUpdateView.as_view(), name='userprofileupdate'),
#    url(r'^userprofiledetail/(?P<slug>[\w\-]+)/$', UserProfileDetailView.as_view(), name='userprofiledetail'),
)
