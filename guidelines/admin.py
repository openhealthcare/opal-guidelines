"""
Admin for Guideline models
"""
from django.contrib import admin
from reversion.admin import VersionAdmin

from guidelines import models

class GuidelineAdmin(VersionAdmin):
    filter_horizontal = 'diagnosis',
    search_fields = 'name',

class GuidelineConsultationAdmin(VersionAdmin):
    list_display= "guideline", "user", "consulted"

admin.site.register(models.Guideline, GuidelineAdmin)
admin.site.register(models.GuidelineConsultation, GuidelineConsultationAdmin)
