from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/location/', views.location, name='location'),
    path('afisha/', views.afisha, name='afisha'),
    path('collectives/', views.collectives, name='collectives'),
]