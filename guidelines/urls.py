"""
Urls for the guidelines OPAL plugin
"""
from django.conf.urls import patterns, url

from guidelines import views

urlpatterns = patterns(
    '',
    url(r'templates/modals/select_guideline.html', views.SelectGuidelineModalView.as_view()),
)
