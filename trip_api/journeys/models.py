from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.

class Journey(models.Model):
    """
    Model for a journey
    """
    start_location = models.PointField(
        geography=True,
        default=Point(0.0, 0.0)
    )
    end_location = models.PointField(
        geography=True,
        default=Point(0.0, 0.0),
    )