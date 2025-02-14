# views.py
from django.shortcuts import render, redirect
from .forms import VehicleTransportRequestForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def request_transport(request):
    if request.method == 'POST':
        form = VehicleTransportRequestForm(request.POST)
        if form.is_valid():
            # Set final_sum to 0 (no calculation for now)
            instance = form.save(commit=False)
            instance.final_sum = 0.00 
            instance.save()
            return redirect('home')
    else:
        form = VehicleTransportRequestForm()

    return render(request, 'request.html', {'form': form})

def contacts(request):
    return render(request, 'contacts.html')

def pricing(request):
    return render(request, 'pricing.html')
