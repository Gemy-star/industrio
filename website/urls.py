from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about', AboutPageView.as_view(), name='about-page'),
    path('services', ServicesPageView.as_view(), name='services-page'),
    path('contact', ContactCreateView.as_view(), name='contact-page'),
    path('contact/details/<pk>', ContactDetailsView.as_view(),
         name='Contact_detail'),

]
