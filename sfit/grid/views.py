from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, render_to_response
from grid.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

@login_required
def grid_edit(request, slug=None):
    if slug: design = get_object_or_404(Design, slug=slug)
    else: design = Design.objects.last()
    u = request.user
    try:
        delta = design.deltas.filter(user=u).latest()
    except ObjectDoesNotExist:
        delta = None
    return render_to_response('base.html', {'design': design, 'delta': delta})

