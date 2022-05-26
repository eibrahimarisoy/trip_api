from core.serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from passengers.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('user', 'device_type')
        extra_kwargs = {
            'device_type': {'write_only': True}
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        passenger = Passenger.objects.create(user=user, **validated_data)
        return passenger


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_again = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
