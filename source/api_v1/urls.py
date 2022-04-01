from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v1.views import QuoteViewSet, get_csrf_token_view, LogoutView

app_name = "api_v1"

router = routers.DefaultRouter()
router.register(r'quote', QuoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("get-csrf-token/", get_csrf_token_view, name='get_csrf_token_view'),
    path("login/", obtain_auth_token, name='api_token_auth'),
    path("logout/", LogoutView.as_view(), name='logout_view'),
]
