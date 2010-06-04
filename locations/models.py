from django.db import models
from django.utils.translation import ugettext_lazy as _

class Campus(models.Model):
    name = models.CharField(blank=False, max_length=150)
    university = models.ForeignKey('University')
    
    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(blank=False, max_length=150, help_text=_("University full name"))
    
    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(blank=False, max_length=150)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    campus = models.ForeignKey('Campus')
    address = models.CharField(blank=True, max_length=500)
    is_main_place = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name