from django.urls import path, include
from rest_framework import routers

from api_v1.views import QuoteViewSet, get_csrf_token_view

app_name = "api_v1"

router = routers.DefaultRouter()
router.register(r'quote', QuoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("get-csrf-token/", get_csrf_token_view),
]
