from django.urls import path
from .views import *

urlpatterns = [
    path('', HotelListView.as_view(), name='list-hotel'),
    path('hotel/<slug:slug>/', HotelDetailView.as_view(), name='detail-hotel'),
    path('list-hotel/hotel/<slug:slug>/booking/', HotelBookingView.as_view(), name='hotel_booking'),  # Nouvelle URL pour la réservation

]
