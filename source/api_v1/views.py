from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
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


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=204)