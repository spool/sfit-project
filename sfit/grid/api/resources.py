from piston.handler import BaseHandler
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from piston.utils import validate, rc
from grid.models import *
from django.contrib.auth import logout
from django.shortcuts import render_to_response, redirect

class DeltaForm(forms.ModelForm):
    class Meta:
        model = Delta
        exclude = ('user', 'design')

class DesignHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    model = Design
    

    def read(self, request, slug=None, timestamp=None, last=None):
        """
        Returns a blogpost, if `slug` is given,
        otherwise all the posts.
        
        Parameters:
         - `slug`: The slug of the post to retrieve.
        """
        if slug:
            design = Design.objects.get(slug=slug)
            if last == 'last':
                try:
                    d = design.deltas.latest()
                except ObjectDoesNotExist:
                    return rc.NOT_HERE
                try:
                    cell = design.deltas.filter(user=request.user).latest().cell
                except ObjectDoesNotExist:
                    cell = -1
                d.cell = cell
                return d

            #elif timestamp:
            #    return design.deltas.get(timestamp=timestamp)
            else:
                return design
        else:
            return Design.objects.all()

    @validate(DeltaForm)
    def create(self, request, slug):
        design = Design.objects.get(slug=slug)
        delta  = Delta.objects.create(user=request.user, design=design)
        delta  = DeltaForm(request.POST, instance=delta)
        delta.save()
        thank_you = "Thanks very much! Feel free to log back in any time and update your piece of the design, and see what your neighbors are up to."
        return redirect('/', {'user': request.user, 'status': thank_you})
