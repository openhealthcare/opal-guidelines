"""
Plugin definition for the guidelines OPAL plugin
"""
from opal.core import plugins

from guidelines import api
from guidelines.urls import urlpatterns

class GuidelinesPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/guidelines/controllers/select_guideline.js'
        ],
        # Add your javascripts here!
        'opal.guidelines': [
            # 'js/guidelines/app.js',
            # 'js/guidelines/controllers/larry.js',
            # 'js/guidelines/services/larry.js',
        ]
    }

    apis = [
        ('guideline', api.GuidelineViewSet),
        ('guideline_consultation', api.ConsultationViewSet)
    ]
