from django.urls import path
from .views import HotelListView, HotelDetailView

urlpatterns = [
    path('', HotelListView.as_view(), name='list-hotel'),
    path('hotel/<slug:slug>/', HotelDetailView.as_view(), name='detail-hotel'),
]
