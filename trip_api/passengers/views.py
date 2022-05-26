from core.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from passengers.models import Passenger
from passengers.serializers import (ChangePasswordSerializer,
                                    PassengerSerializer)


class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")

            if not self.object.check_password(old_password):
                return Response(
                    {"old_password": [_('Wrong password.')]},
                    status=status.HTTP_400_BAD_REQUEST
                )

            new_password = serializer.data.get("new_password")
            new_password_again = serializer.data.get("new_password_again")

            if new_password != new_password_again:

                return Response(
                    {"New Password": [_('The passwords you enter must match.')]},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # set_password also hashes the password that the user will get
            self.object.set_password(new_password)
            self.object.save()

            return Response(
                {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': [_('Password updated successfully')]
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
