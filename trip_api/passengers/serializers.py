from core.serializers import UserSerializer
from passengers.models import Passenger
from rest_framework import serializers


class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('user',)
