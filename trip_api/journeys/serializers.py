from rest_framework import serializers

from journeys.models import Journey
from passengers.serializers import PassengerSerializer


class JourneySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Journey
        fields = (
            "uuid", "passenger", "origin", "destination", "distance",
            "duration", "start_time", "end_time",
        )
        extra_kwargs = {
            "uuid": {"read_only": True},
            "passenger": {"read_only": True},
            "distance": {"read_only": True},
            "duration": {"read_only": True},
        }


class JourneyDetailSerializer(JourneySerializer):
    passenger = PassengerSerializer(read_only=True)