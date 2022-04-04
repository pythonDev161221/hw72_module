import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
import webapp.models
from api_v1.serializers import QuoteSerializer
from webapp.models import Quote


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_permissions(self):
        if self.request.method == "POST":
            return []
        elif self.request.method == "GET":
            if self.request.user.is_staff:
                return []
            else:
                self.queryset = Quote.objects.filter(status__exact="moderated")
                return []
        elif self.request.method == "PUT":
            QuoteSerializer.Meta.read_only_fields = ("id", "rating", "created_at", "name", "email")
            return super().get_permissions()
        elif self.request.method == "DELETE":
            return super(QuoteViewSet, self).get_permissions()
        return super().get_permissions()


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


class LikeView(APIView):
    print('sef')
    def post(self, request, *args, **kwargs):
        print(kwargs)
        print(kwargs.get('pk'))

        quote = Quote.objects.get(pk=kwargs.get('pk'))
        print(quote.name)
        quote.rating += 1
        quote.save()
        print(quote.rating)
        # try:
        #
        # except ValueError:
        #     return Response({'error': 'error'}, status=400)

        return Response(status=204)