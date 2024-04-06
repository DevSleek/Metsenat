from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import SponsorForStudent


@receiver(pre_save, sender=SponsorForStudent) 
def checker(sender, instance, **kwargs):
    if sender.objects.
