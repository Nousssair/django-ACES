# home_page_static/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('list_hotel/', HotelListView.as_view(), name='lite_hotel'),
]