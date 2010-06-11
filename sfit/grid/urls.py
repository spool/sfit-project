from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from grid.models import Design

design_dict = {
        'design' : Design.objects.latest(),
        }

urlpatterns = patterns('',
        (r'^api/', include('sfit.grid.api.urls')),
        (r'^', direct_to_template, {'template': 'base.html', 'extra_context': design_dict}),
        )
