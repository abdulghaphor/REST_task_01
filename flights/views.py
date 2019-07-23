from .models import *
from rest_framework.generics import ListAPIView
from .serializers import *
from datetime import date

class FlightList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

class BookingList(ListAPIView):
	queryset = Booking.objects.filter(date__gt=date.today())
	serializer_class = BookingSerializer