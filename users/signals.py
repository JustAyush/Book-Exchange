from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Dashboard

@receiver(post_save, sender=User)
def create_dashboard(sender, instance, created, **kwargs):
    if created:
        Dashboard.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_dashboard(sender, instance, **kwargs):
    instance.dashboard.save()
