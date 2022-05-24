from django.db import models


class Passenger(models.Model):
    user = models.OneToOneField(
        'core.User',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"

    def __str__(self):
        return f"{self.user.get_full_name()}"
