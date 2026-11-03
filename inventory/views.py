from rest_framework import generics
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer


# List all vehicles and create a new vehicle
class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):

        queryset = Vehicle.objects.all()

        brand = self.request.query_params.get('brand')
        fuel_type = self.request.query_params.get('fuel_type')
        is_available = self.request.query_params.get('is_available')

        if brand:
            queryset = queryset.filter(brand__iexact=brand)

        if fuel_type:
            queryset = queryset.filter(fuel_type=fuel_type)

        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')

        return queryset


# View, update and delete a single vehicle
class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# List all bookings and create a new booking
class BookingListCreateView(generics.ListCreateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# View a single booking
class BookingDetailView(generics.RetrieveAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer