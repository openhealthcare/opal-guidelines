"""
Admin for Guideline models
"""
from django.contrib import admin
import reversion

from guidelines import models

class GuidelineAdmin(reversion.VersionAdmin):
    filter_horizontal = 'diagnosis',
    search_fields = 'name',

class GuidelineConsultationAdmin(reversion.VersionAdmin):
    list_display= "guideline", "user", "consulted"

admin.site.register(models.Guideline, GuidelineAdmin)
admin.site.register(models.GuidelineConsultation, GuidelineConsultationAdmin)
