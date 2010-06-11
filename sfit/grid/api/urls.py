from django.conf.urls.defaults import *
from piston.resource import Resource
from grid.api.resources import DeltaHandler

delta_handler = Resource(DeltaHandler)

urlpatterns = patterns('',
        url(r'^netjs/$', node_handler),
        url(r'^netjs/(?P<slug>[^/]+)/$', node_handler),
        )

