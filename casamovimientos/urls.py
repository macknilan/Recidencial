from django.conf.urls import patterns, url
from .views import ResumeView

urlpatterns = patterns('',
     url(r'^summaryaccounts/(?P<slug>[\w\-]+)/$', ResumeView.as_view(), name='summaryaccounts'),
)
