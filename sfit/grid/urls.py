from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^api/', include('sfit.grid.api.urls'))
        )
