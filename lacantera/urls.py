from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lacantera.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('casamovimientos.urls')),
    url(r'', include('casagenerales.urls')),
    url(r'', include('compradores.urls')),
    url(r'', include('userprofiles.urls')),
)

# PARA SERVIR LOS ARCHIVOS DE MEDIA EN DESARROLLO "NO EN PRODUCCION" CUANDO DEGUB ESTA EN TRUE
# if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
#        )

# PARA SERVIR LOS ARCHIVOS DE MEDIA EN DESARROLLO "NO EN PRODUCCION" CUANDO DEGUB ESTA EN TRUE
#if settings.DEBUG:
#  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
