from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.study,name = 'study'),
    path('index/', views.index, name='index'),
    path('background/',views.background, name = 'background change'),
    path('country/',views.country, name = 'country'),
    path('contact/',views.contact, name = 'contact'),
    path('address/',views.address,name = 'address')
]