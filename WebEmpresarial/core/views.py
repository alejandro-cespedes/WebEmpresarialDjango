from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.

class inicioPageView(TemplateView):
    template_name = 'core/inicio.html'

class AboutPageView(TemplateView):
    template_name = 'core/about.html'

class StorePageView(TemplateView):
    template_name = 'core/store.html'




