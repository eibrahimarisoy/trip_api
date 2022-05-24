from core.serializers import UserSerializer
from rest_framework import serializers

from passengers.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        passenger = Passenger.objects.create(user=user)
        return passenger
