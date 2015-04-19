from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'zaklady.views.glowna', name = 'glowna'),
)