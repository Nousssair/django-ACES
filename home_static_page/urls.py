# home_page_static/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('faq/', FaqPageView.as_view(), name='faq_page'),
]