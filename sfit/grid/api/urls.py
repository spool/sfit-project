from django.conf.urls.defaults import *
from piston.resource import Resource
from grid.api.resources import DeltaHandler

delta_handler = Resource(DeltaHandler)

urlpatterns = patterns('',
        url(r'^grid/$', design_handler),
        url(r'^grid/(?P<slug>[^/]+)/$', design_handler),
        url(r'^grid/(?P<slug>[^/]+)/(?P<timestamp>[^/]+)/$', design_handler),
        )

