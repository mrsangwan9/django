from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creator/',views.creator, name = 'creator'),
    path ('study/',views.study, name ='study'),
    path('country/',views.country, name = 'country'),
    path('contact/',views.contact, name = 'contact'),
    path('address/',views.address,name = 'address')
]