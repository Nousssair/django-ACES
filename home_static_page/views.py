from django.shortcuts import render

# home_page_static/views.py
from django.views.generic import TemplateView

# Définir la vue CBV pour afficher "Hello"
class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name= 'contact.html'
    
class FaqPageView(TemplateView):
    template_name= 'faq.html'