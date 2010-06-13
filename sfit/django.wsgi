import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'sfit.settings'
os.environ['PYTHON_EGG_CACHE'] = "/var/www/vhosts/complex.org.uk/subdomains/sfit/apps/.egg"
sys.path.append('/var/www/vhosts/complex.org.uk/subdomains/sfit/apps/sfit-project')
sys.path.append('/var/www/vhosts/complex.org.uk/subdomains/sfit/apps/sfit-project/sfit')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

