from django.conf.urls.defaults import *
from piston.resource import Resource
from grid.api.resources import DesignHandler

design_handler = Resource(DesignHandler)

urlpatterns = patterns('',
        url(r'^(?P<slug>[^/]+)/$', design_handler),
        url(r'^(?P<slug>[^/]+)/(?P<timestamp>[^/]+)/$', design_handler),
        url(r'^$', design_handler),
        )

