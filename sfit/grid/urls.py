from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from grid.models import Design
from grid.views import grid_edit

design_dict = {
        'design' : Design.objects.last(),
        }

urlpatterns = patterns('',
        (r'^api/', include('sfit.grid.api.urls')),
        #(r'^', direct_to_template, {'template': 'base.html', 'extra_context': design_dict}),
        (r'^', grid_edit),
        )
