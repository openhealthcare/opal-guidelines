"""
Models for guidelines
"""
from django.contrib.auth.models import User
from django.db import models
from opal.models import Condition

class Guideline(models.Model):
    """
    Our basic model representing a Clinical Guideline.
    
    We will associate it with a diagnosis.
    """
    name      = models.CharField(max_length=200)
    link      = models.URLField(blank=True, null=True)
    diagnosis = models.ManyToManyField(Condition, help_text="Canonical terms only")
    source    = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    
class GuidelineConsultation(models.Model):
    """
    Record occasions on which users have consulted guidelines.
    """
    guideline   = models.ForeignKey(Guideline)
    user        = models.ForeignKey(User)
    consulted  = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u'{0} consulted by {1} on {2}'.format(
            self.guideline.name, self.user, self.consulted)
