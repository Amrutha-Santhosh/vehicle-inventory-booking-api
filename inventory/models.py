from django.db import models


class Vehicle(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


class Booking(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):
        if self.vehicle_id and self.start_date and self.end_date:
            days = (self.end_date - self.start_date).days
            self.total_amount = days * self.vehicle.price_per_day

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle}"