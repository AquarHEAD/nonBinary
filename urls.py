from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^nonBinary/', include('nonBinary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'nonBinary.lifestat.views.home'),
    (r'^newstat/$', 'nonBinary.lifestat.views.new'),
    (r'^delete/(?P<stat_id>\d+)/$', 'nonBinary.lifestat.views.delete'),
    (r'^admin/', include(admin.site.urls)),
)
