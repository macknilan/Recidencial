from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('casamovimientos.urls')),
    url(r'', include('casagenerales.urls')),
    url(r'', include('compradores.urls')),
    url(r'', include('userprofiles.urls')),
)

if settings.DEBUG:
	"""
	PARA SERVIR LOS ARCHIVOS DE MEDIA EN DESARROLLO "NO EN PRODUCCION" CUANDO DEGUB ESTA EN TRUE
	"""
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        )

if settings.DEBUG:
	"""
	PARA SERVIR LOS ARCHIVOS DE MEDIA EN DESARROLLO "NO EN PRODUCCION" CUANDO DEGUB ESTA EN TRUE
	"""
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
