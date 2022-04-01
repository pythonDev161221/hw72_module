from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from api_v1.serializers import QuoteSerializer
from webapp.models import Quote


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    