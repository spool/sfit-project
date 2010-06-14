from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core import validators

class TimeSeriesManager(models.Manager):

    def last(self):
        try:
            return self.latest()
        except:
            return None

    def first(self):
        try:
            return self.all()[0]
        except:
            return None

class Delta(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    edges_h   = models.CharField(max_length=4096,
            validators = [validators.RegexValidator(r'[01]{4096}')])
    edges_v   = models.CharField(max_length=4096,
            validators = [validators.RegexValidator(r'[01]{4096}')])
    diag_se   = models.CharField(max_length=4096,
            validators = [validators.RegexValidator(r'[01]{4096}')])
    diag_sw   = models.CharField(max_length=4096,
            validators = [validators.RegexValidator(r'[01]{4096}')])
    cell      = models.PositiveSmallIntegerField(blank=True, null=True)
    user      = models.ForeignKey(User, related_name='deltas')
    design    = models.ForeignKey('Design', related_name='deltas')
    objects   = TimeSeriesManager()

    def __unicode__(self):
        return '%s: %s' % (self.user, self.timestamp)

    class Meta:
        get_latest_by = "timestamp"
        ordering = ['timestamp']

class Design(models.Model):
    slug      = models.SlugField(unique=True)
    name      = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects   = TimeSeriesManager()

    def __unicode__(self):
        return self.name

    class Meta:
        get_latest_by = "timestamp"
        ordering = ['timestamp']

class DeltaInline(admin.TabularInline):
    model = Delta

class DesignAdmin(admin.ModelAdmin):
    inlines = [DeltaInline]

admin.site.register(Design, DesignAdmin)
