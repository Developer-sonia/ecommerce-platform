from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to Ecommerce Platform',
            'Thank you for signing up.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )