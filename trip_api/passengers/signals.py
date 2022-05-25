from django.db.models.signals import post_save
from django.dispatch import receiver
from core.tasks import send_email_task

from passengers.models import Passenger

from django.utils.translation import gettext_lazy as _


@receiver(post_save, sender=Passenger)
def sned_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Send welcome email
        send_email_task.delay(
            subject=_("Welcome to the Passenger App"),
            message=_("Welcome to the Passenger App"),
            from_email=None,
            recipient_list=[instance.user.email],
        )
