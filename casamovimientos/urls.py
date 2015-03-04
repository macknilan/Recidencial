from django.conf.urls import patterns, url
from .views import ResumeView

urlpatterns = patterns('',

     url(r'^summaryaccounts/(?P<slug>[\w\-]+)/$', ResumeView.as_view(), name='summaryaccounts'),
#    url(r'^userupdate/(?P<slug>[\w\-]+)/$', UserUpdateView.as_view(), name='userupdate'),
#    url(r'^userprofileupdate/(?P<slug>[\w\-]+)/$', UserProfileUpdateView.as_view(), name='userprofileupdate'),
#    url(r'^userprofiledetail/(?P<slug>[\w\-]+)/$', UserProfileDetailView.as_view(), name='userprofiledetail'),     
)
