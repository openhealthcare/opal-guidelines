"""
Models for guidelines
"""
from django.db import models
from opal.models import ConditionLookupList

class Guideline(models.Model):
    name      = models.CharField(max_length=200)
    link      = models.URLField(blank=True, null=True)
    diagnosis = models.ManyToManyField(ConditionLookupList,
                                       help_text="Canonical terms only")
    source    = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
    
