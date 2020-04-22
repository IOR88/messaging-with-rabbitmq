from django.views import generic
from rest_framework import views, response, viewsets, status
import django_filters.rest_framework as django_filters
from django.contrib.auth import models as auth_models
from chat import models, serializers


class BaseView(generic.TemplateView):
    template_name = 'base.html'


class ActiveUsers(views.APIView):

    def get(self, rquest):
        queryset = auth_models.User.objects.filter(is_active=True)
        return response.Response(queryset.values_list('username', flat=True))


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_fields = {
        'user': ('exact',),
        'room': ('exact',)
    }