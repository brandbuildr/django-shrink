from shrink.conf import settings
from django.conf.urls.defaults import patterns


urlpatterns = []


if settings.DEBUG:
    urlpatterns += patterns('', (
        r'^%s/(?P<path>.*\.scss)$' % settings.STATIC_URL.strip('/'),
        'shrink.views.scss'
        ))

