from django.urls import path

from .views import (
    VehicleListCreateView,
    VehicleDetailView,
    BookingListCreateView,
    BookingDetailView
)

urlpatterns = [

    # Vehicle APIs
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list'),

    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),

    # Booking APIs
    path('bookings/', BookingListCreateView.as_view(), name='booking-list'),

    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

]