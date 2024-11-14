from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from hotel.filters import HotelFilter
from .models import *

# Vue pour afficher la liste des hôtels
class HotelListView(ListView):
    model = Hotel
    template_name = 'list-hotel.html'
    context_object_name = 'hotels'
    paginate_by = 10  # Affiche 10 hôtels par page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ajouter une liste d'étoiles à chaque hôtel dans le contexte
        for hotel in context['hotels']:
            hotel.stars_range = range(hotel.stars)  # Liste d'étoiles pleines
            hotel.stars_empty_range = range(6 - hotel.stars)  # Liste d'étoiles vides
        
        # Ajouter le formulaire de filtrage au contexte pour l'utiliser dans le template
        context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset()).form
        return context
    
    def get_queryset(self):
        queryset = Hotel.objects.all()
        
        # Appliquer les filtres via HotelFilter
        hotel_filter = HotelFilter(self.request.GET, queryset=queryset)
        return hotel_filter.qs  # Retourne les hôtels filtrés
    

# Vue pour afficher les détails d'un hôtel
class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'detail-hotel.html'
    context_object_name = 'hotel'
    def get_object(self, queryset=None):
        return get_object_or_404(Hotel, slug=self.kwargs['slug'])
