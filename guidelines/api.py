"""
API for the Guidelines plugin
"""
from opal.core.views import ModelViewSet
from rest_framework import permissions, serializers, status

from guidelines.models import Guideline, GuidelineConsultation

class GuidelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guideline

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidelineConsultation
        
class GuidelineViewSet(ModelViewSet):
    queryset = Guideline.objects.all()
    serializer_class = GuidelineSerializer

    
class ConsultationViewSet(ModelViewSet):
    queryset = GuidelineConsultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def create(self, request):
        request.data['user'] = request.user.id
        if 'where' in request.data and 'guideline' not in request.data:
            guideline = Guideline.objects.get(link=request.data['where'])
            request.data['guideline'] = guideline.id
        return super(ConsultationViewSet, self).create(request)
