# home_page_static/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', HotelListView.as_view(), name='list-hotel'),
    path('hotel/<slug:slug>/', HotelDetailView.as_view(), name='detail-hotel'),
]