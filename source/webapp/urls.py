from django.urls import path, include

app_name = 'webapp'

urlpatterns = [
    path('', include('webapp.urls')),
]