from django.urls import path, include

from webapp.views import QuoteListView

app_name = 'webapp'

urlpatterns = [
    path('', QuoteListView.as_view(), name="quote_list_view"),
]
