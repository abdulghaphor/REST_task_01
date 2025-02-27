from rest_framework import serializers
from .models import *

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination','time','price',]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight','date','id']