"""
Views for the guidelines OPAL Plugin
"""
from django.views.generic import TemplateView

# You might find these helpful ! 
# from opal.core.views import LoginRequiredMixin, _build_json_response

class SelectGuidelineModalView(TemplateView):
    template_name = 'modals/select_guideline.html'

    def get_context_data(self, **kwargs):
        context = super(SelectGuidelineModalView, self).get_context_data(**kwargs)
        from guidelines.models import Guideline
        context['guidelines'] = Guideline.objects.all()
        print context
        return context
