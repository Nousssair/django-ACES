import django_filters
from django import forms
from .models import *

class HotelFilter(django_filters.FilterSet):
    # Filtrer par nom de l'hôtel
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',  # Recherche insensible à la casse
        label='Hotel Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Filtrer par type de chambre
    room_type = django_filters.ChoiceFilter(
        choices=Hotel.ROOM_TYPES,
        label='Room Type',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Filtrer par note de l'hôtel (rating)
    rating = django_filters.NumberFilter(
        field_name='rating',
        lookup_expr='exact',  # Recherche par valeur exacte
        label='Rating',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    # Filtrer par catégorie de l'hôtel
    category = django_filters.ChoiceFilter(
        choices=Hotel.CATEGORY_CHOICES,
        label='Category',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Filtrer par prix par adulte (utilise le modèle HotelBooking)
    # Notez que ce filtre sera basé sur le modèle HotelBooking, pas directement sur Hotel.
    amount_per_adult = django_filters.NumberFilter(
        field_name='bookings__amount_per_adult',  # Utilisation de la relation bookings
        lookup_expr='lte',  # Recherche des prix inférieurs ou égaux
        label='Max Price per Adult',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Hotel
        fields = ['name', 'room_type', 'rating', 'category', 'amount_per_adult']
