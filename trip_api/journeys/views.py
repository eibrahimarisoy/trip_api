from rest_framework import viewsets

from journeys.models import Journey
from journeys.serializers import JourneyDetailSerializer, JourneySerializer


class JourneyViewset(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

    def get_queryset(self):
        return self.queryset.filter(
            passenger=self.request.user.passenger,
        )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return JourneyDetailSerializer

        return super().get_serializer_class()


    def perform_create(self, serializer):
        serializer.save(
            passenger=self.request.user.passenger,    
        )
