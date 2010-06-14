from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, render_to_response
from grid.models import *

@login_required
def grid_edit(request, slug=None):
    if slug: d = get_object_or_404(Design, slug=slug)
    else: d = Design.objects.last()
    status = "Welcome to the t-shirt designer, a micro-project produced as part of the SFI Complex Systems Summer School 2010. Your segment is indicated by the red boundary, with your neighbours on each side. Make (and erase) marks by dragging the mouse from point to point. Your session will automatically time out after 3 minutes, so work quickly!"
    return render_to_response('index.html', {'design': d,
                                             'user': request.user,
                                             'status': status})

