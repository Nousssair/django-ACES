from django import forms
from .models import *

class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = [
            'hotel',  # L'hôtel sera sélectionné par l'utilisateur
            'order_number',  # Le numéro de commande sera généré automatiquement
            'check_in',
            'check_out',
            'number_of_adults',
            'number_of_children',
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'number_of_adults': forms.NumberInput(attrs={'min': 1}),
            'number_of_children': forms.NumberInput(attrs={'min': 0}),
        }

    # Ajout des champs pour le nom complet et l'email
    full_name = forms.CharField(max_length=100, required=True, label='Full Name')
    email = forms.EmailField(required=True, label='Email')
    
    # Liste des âges des enfants
    children_ages = forms.CharField(widget=forms.Textarea, required=False, label="Children's Ages (comma separated)")

    def clean(self):
        cleaned_data = super().clean()

        # Calcul du montant total
        number_of_adults = cleaned_data.get('number_of_adults')
        number_of_children = cleaned_data.get('number_of_children')
        
        if number_of_adults is not None and number_of_children is not None:
            hotel = cleaned_data.get('hotel')
            if hotel:
                amount_per_adult = hotel.amount_per_adult
                amount_per_child = hotel.amount_per_child

                total_amount_adult = amount_per_adult * number_of_adults
                total_amount_children = amount_per_child * number_of_children

                total_amount = total_amount_adult + total_amount_children

                cleaned_data['total_amount_adult'] = total_amount_adult
                cleaned_data['total_amount_children'] = total_amount_children
                cleaned_data['total_amount'] = total_amount

        return cleaned_data
