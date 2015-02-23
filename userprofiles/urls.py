from django.conf.urls import patterns, url

from .views import HomeRedirectView, LoginView, ProfileView, PerfilRedirectView, EditUser_UserProfileDef

urlpatterns = patterns('',

    url(r'^$', HomeRedirectView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^profile/(?P<slug>[\w\-]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
    url(r'^edituseruserprofile/$', EditUser_UserProfileDef, name='edituseruserprofile'),
#    url(r'^userupdate/(?P<slug>[\w\-]+)/$', UserUpdateView.as_view(), name='userupdate'),
#    url(r'^userprofileupdate/(?P<slug>[\w\-]+)/$', UserProfileUpdateView.as_view(), name='userprofileupdate'),
#    url(r'^userprofiledetail/(?P<slug>[\w\-]+)/$', UserProfileDetailView.as_view(), name='userprofiledetail'),
)
