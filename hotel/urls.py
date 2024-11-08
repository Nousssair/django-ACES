from django.views.generic import TemplateView

# Définir la vue CBV pour afficher "Hello"
class HotelListView(TemplateView):
    template_name = 'list_hotel.html'