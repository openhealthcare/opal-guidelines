"""
Urls for the guidelines Opal plugin
"""
from django.conf.urls import url

from guidelines import views

urlpatterns = [
    url(r'templates/modals/select_guideline.html', views.SelectGuidelineModalView.as_view()),
]
