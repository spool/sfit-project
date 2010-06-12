from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from grid.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^grid/', include('sfit.grid.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^users/', profile),
    (r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'^$', grid_edit),
)
