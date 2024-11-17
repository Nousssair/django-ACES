from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView , View
from hotel.filters import HotelFilter
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import  HotelBookingForm


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
        hotel_filter = HotelFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = hotel_filter
        
        
        #verificaiton si acun résultat trouvé :
        if not hotel_filter.qs.exists():
            messages.info(self.request, 'Not exist in search')
            
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
    
    def get_context_data(self, **kwargs):
        # Récupérer le contexte de la vue DetailView par défaut
        context = super().get_context_data(**kwargs)
        
        # Ajouter les réservations associées à l'hôtel dans le contexte
        hotel = self.get_object()
        bookings = HotelBooking.objects.filter(hotel=hotel)  # Récupérer les réservations pour cet hôtel
        context['bookings'] = bookings  # Ajouter les réservations au contexte
        
        return context
    
    






class HotelBookingView(View):
    def get(self, request, *args, **kwargs):
        # Récupérer l'hôtel (à partir du slug, par exemple)
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])
        
        # Créer le formulaire
        form = HotelBookingForm(initial={'hotel': hotel})
        
        # Afficher le formulaire dans le template
        return render(request, 'hotel_booking_form.html', {'form': form, 'hotel': hotel})

    def post(self, request, *args, **kwargs):
        # Récupérer l'hôtel (à partir du slug, par exemple)
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])

        # Créer le formulaire avec les données soumises
        form = HotelBookingForm(request.POST)

        # Si le formulaire est valide
        if form.is_valid():
            # Sauvegarder la réservation
            booking = form.save(commit=False)
            booking.hotel = hotel  # Associer l'hôtel à la réservation
            booking.save()

            # Afficher un message de confirmation ou rediriger
            return render(request, 'booking_confirmation.html', {'booking': booking})
        
        # Si le formulaire n'est pas valide, on le renvoie avec les erreurs
        return render(request, 'hotel_booking_form.html', {'form': form, 'hotel': hotel})

    
