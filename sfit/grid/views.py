from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, render_to_response
from grid.models import *

@login_required
def grid_edit(request, slug=None):
    if slug: d = get_object_or_404(Design, slug=slug)
    else: d = Design.objects.last()
    status = "Welcome to the t-shirt designer, a micro-project produced as part of the SFI Complex Systems Summer School 2010. Through this interface, you can make changes to your design, which will be one part of a larger piece."
    return render_to_response('index.html', {'design': d,
                                             'user': request.user,
                                             'status': status})

