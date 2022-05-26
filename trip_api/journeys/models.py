from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from core.models import BaseModel
# Create your models here.
from django.contrib.gis.db.models.functions import Distance

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
        geography=True,
        default=Point(0, 0),
        null=True,
        blank=True,
    )
    destination = models.PointField(
        geography=True,
        default=Point(0, 0),
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
    
    def save(self, *args, **kwargs):
        if self.distance is None and self.origin and self.destination:
            self.distance = self.origin.distance(self.destination)

        if self.duration is None and self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time

        return super(Journey, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.passenger.user.get_full_name()} - {self.start_time}"
