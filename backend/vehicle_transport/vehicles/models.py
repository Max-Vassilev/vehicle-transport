from django.db import models

class VehicleTransportRequest(models.Model):
    STATUS_CHOICES = [
        ('pending_approval', 'Pending Approval'),
        ('approved', 'Approved'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    pickup_country = models.CharField(max_length=100)
    pickup_city = models.CharField(max_length=100)
    delivery_country = models.CharField(max_length=100, default='Bulgaria')
    delivery_city = models.CharField(max_length=100, default='Sofia')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending_approval'
    )
    
    small_car_count = models.PositiveIntegerField(default=0)
    big_car_count = models.PositiveIntegerField(default=0)
    suv_count = models.PositiveIntegerField(default=0)
    bus_count = models.PositiveIntegerField(default=0)
    
    final_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.first_name} {self.last_name}"
