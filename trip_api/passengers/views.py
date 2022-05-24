from passengers.serializers import PassengerSerializer
from rest_framework import viewsets

from passengers.models import Passenger

# Create your views here.
class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)