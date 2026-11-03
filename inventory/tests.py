
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Vehicle, Booking


class VehicleAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vehicle = Vehicle.objects.create(
            name="Fortuner",
            brand="Toyota",
            year=2022,
            price_per_day=3000,
            fuel_type="Diesel",
            is_available=True
        )

    def test_vehicle_list(self):
        response = self.client.get('/api/vehicles/')
        self.assertEqual(response.status_code, 200)

    def test_create_vehicle(self):
        data = {
            "name": "Swift",
            "brand": "Maruti",
            "year": 2023,
            "price_per_day": "1500.00",
            "fuel_type": "Petrol",
            "is_available": True
        }
        response = self.client.post(
            '/api/vehicles/', data, format='json'
        )
        self.assertEqual(response.status_code, 201)


class BookingAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vehicle = Vehicle.objects.create(
            name="Fortuner",
            brand="Toyota",
            year=2022,
            price_per_day=3000,
            fuel_type="Diesel",
            is_available=True
        )

    def test_create_booking(self):
        data = {
            "vehicle": self.vehicle.id,
            "customer_name": "Test Customer",
            "customer_phone": "9876543210",
            "start_date": "2026-11-10",
            "end_date": "2026-11-12"
        }
        response = self.client.post(
            '/api/bookings/', data, format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data['total_amount'], "6000.00"
        )

    def test_invalid_phone_number(self):
        data = {
            "vehicle": self.vehicle.id,
            "customer_name": "Test Customer",
            "customer_phone": "12345",
            "start_date": "2026-11-10",
            "end_date": "2026-11-12"
        }
        response = self.client.post(
            '/api/bookings/', data, format='json'
        )
        self.assertEqual(response.status_code, 400)
