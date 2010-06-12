from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, render_to_response
from grid.models import *

@login_required
def grid_edit(request, slug=None):
    if slug: d = get_object_or_404(Design, slug=slug)
    else: d = Design.objects.last()
    return render_to_response('base.html', {'design': d})

