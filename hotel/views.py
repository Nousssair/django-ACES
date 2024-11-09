from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *

# Vue pour afficher la liste des hôtels
class HotelListView(ListView):
    model = Hotel
    template_name = 'list-hotel.html'
    context_object_name = 'hotels'

# Vue pour afficher les détails d'un hôtel
class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'detail-hotel.html'
    context_object_name = 'hotel'
    def get_object(self, queryset=None):
        return get_object_or_404(Hotel, slug=self.kwargs['slug'])
