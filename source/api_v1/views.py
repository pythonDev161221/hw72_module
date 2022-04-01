from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from api_v1.serializers import QuoteSerializer
from webapp.models import Quote


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])