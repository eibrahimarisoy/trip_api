import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from passengers.managers import CustomUserManager

from core.enums import StatusEnum


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    status = models.SmallIntegerField(
        default=StatusEnum.ACTIVE,
        choices=StatusEnum.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    """
    Model for a user
    """

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.get_full_name()}"
