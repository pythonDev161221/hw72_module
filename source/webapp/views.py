from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Quote


class QuoteListView(ListView):
    model = Quote
    template_name = 'quote_list_view.html'
