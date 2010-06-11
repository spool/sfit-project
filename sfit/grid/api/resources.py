from piston.handler import BaseHandler
from grid.models import *

class DesignHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    model = Design

    def read(self, request, slug=None, timestamp=None):
        """
        Returns a blogpost, if `slug` is given,
        otherwise all the posts.
        
        Parameters:
         - `slug`: The slug of the post to retrieve.
        """
        if slug:
            design = Design.objects.get(slug=slug)
            if timestamp:
                return design.deltas.get(timestamp=timestamp)
            else:
                return design
        else:
            return Design.objects.all()
        
