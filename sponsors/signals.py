from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from students.models import SponsorForStudent

@receiver(pre_save, sender=SponsorForStudent)
def check(self, instance,  *args, **kwargs):
    sponsor_left = instance.student_sponsor.sponsorship_sum - instance.sponsor.spent_sum
    student_left = instance.student.contract_sum - instance.student.allocated_sum
    if instance.sponsor_allocated_sum > sponsor_left or instance.sponsor_allocated_sum > student_left:
        raise ValidationError(
        "Allocated sum incorrect"
    )

@receiver(post_save, sender=SponsorForStudent)
def save(self, instance, created, *args, **kwargs):
    if created:
        instance.sponsor.spent_sum += instance.allocated_sum
        instance.sponsor.save()

        instance.student.allocated_sum += instance.allocated_sum
        instance.student.save()
