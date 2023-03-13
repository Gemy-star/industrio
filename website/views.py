from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'website/home_page.html'


class AboutPageView(TemplateView):
    template_name = 'website/about_page.html'


class ServicesPageView(TemplateView):
    template_name = 'website/services_page.html'
