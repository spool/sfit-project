from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Delta(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    edges_h   = models.CharField(max_length=4160)
    edges_v   = models.CharField(max_length=4160)
    diag_se   = models.CharField(max_length=4096)
    diag_sw   = models.CharField(max_length=4096)
    cell      = models.PositiveSmallIntegerField(blank=True, null=True)
    user      = models.ForeignKey(User, null=True, related_name='deltas')

    def __unicode__(self):
        return '%s: %s' % (self.user, self.timestamp)

class Design(models.Model):
    slug      = models.SlugField()
    name      = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    deltas    = models.ForeignKey('Delta', related_name='design')

    def __unicode__(self):
        return self.name
