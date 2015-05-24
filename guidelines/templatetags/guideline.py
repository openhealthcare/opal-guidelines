"""
Template helpers for guidelines
"""
from django import template
from opal.models import ConditionLookupList

from guidelines.models import Guideline

register = template.Library()

@register.inclusion_tag('guidelines/guideline_for.html')
def guideline_for(where):
    guidelines = Guideline.objects.all()
    items = ConditionLookupList.objects.filter(
        guideline__in=guidelines
    ).values_list('name', flat=True)
    return dict(where=where, items=items)

