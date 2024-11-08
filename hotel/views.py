from django.views.generic import TemplateView

# Définir la vue CBV pour afficher "Hello"
class HotelListView(TemplateView):
    template_name = 'list-hotel.html'
    

class HotelDetailView(TemplateView):
    template_name = 'detail-hotel.html'