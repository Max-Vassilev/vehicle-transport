from django import forms
from .models import VehicleTransportRequest

class VehicleTransportRequestForm(forms.ModelForm):
    class Meta:
        model = VehicleTransportRequest
        fields = [
            'first_name', 'last_name', 'phone', 
            'pickup_country', 'pickup_city', 
            'delivery_country', 'delivery_city',  # Added new fields here
            'small_car_count', 'big_car_count', 
            'suv_count', 'bus_count'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'pickup_country': forms.TextInput(attrs={'placeholder': 'Pickup Country'}),
            'pickup_city': forms.TextInput(attrs={'placeholder': 'Pickup City'}),
            'delivery_country': forms.TextInput(attrs={'placeholder': 'Delivery Country'}),  # Placeholder for delivery country
            'delivery_city': forms.TextInput(attrs={'placeholder': 'Delivery City'}),          # Placeholder for delivery city
            'small_car_count': forms.NumberInput(attrs={'min': 0}),
            'big_car_count': forms.NumberInput(attrs={'min': 0}),
            'suv_count': forms.NumberInput(attrs={'min': 0}),
            'bus_count': forms.NumberInput(attrs={'min': 0}),
        }
