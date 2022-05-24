from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from core.models import BaseModel
# Create your models here.

class Journey(BaseModel):
    """
    Model for a journey
    """
    passenger = models.ForeignKey(
        'passengers.Passenger',
        on_delete=models.CASCADE,
        related_name='journeys',
    )
    origin = models.PointField(
        srid=4326,
        null=True,
        blank=True,
    )
    destination = models.PointField(
        srid=4326,
        null=True,
        blank=True,
    )
    distance = models.FloatField(
        null=True,
        blank=True,
    )
    duration = models.FloatField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        null=True,
        blank=True,
    )
    start_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    end_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"

    def __str__(self):
        return f"{self.passenger.user.get_full_name()} - {self.start_time}"
