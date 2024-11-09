from django.views.generic import TemplateView
from .models import *

# Définir la vue CBV pour afficher "Hello"
class HotelListView(TemplateView):
    Model = Hotel
    template_name = 'list-hotel.html'
    content_type = 'hotels'
    

class HotelDetailView(TemplateView):
    Model = Hotel
    template_name = 'detail-hotel.html'
    content_type = 'hotel'