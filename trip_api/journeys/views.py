from django.shortcuts import render
from rest_framework import viewsets

from journeys.models import Journey
from journeys.serializers import JourneySerializer

# Create your views here.

class JourneyViewset(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

    def perform_create(self, serializer):
        serializer.save(
            passenger=self.request.user.passenger,    
        )