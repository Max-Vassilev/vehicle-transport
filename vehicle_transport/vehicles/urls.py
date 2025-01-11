from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('request/', views.request_transport, name='request'), 
    path('contacts/', views.contacts, name='contacts'),
    path('pricing/', views.pricing, name='pricing'), 
]