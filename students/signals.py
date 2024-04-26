from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from students.models import SponsorForStudent


@receiver(pre_save, sender=SponsorForStudent)
def check(instance, *args, **kwargs):
    sponsor_left = int(instance.student_sponsor.sponsorship_sum) - int(instance.student_sponsor.spent_sum)
    student_left = int(instance.student.contract_sum) - int(instance.student.allocated_sum)
    if int(instance.sponsor_allocated_sum) > sponsor_left or int(instance.sponsor_allocated_sum) > student_left:
        raise ValidationError(
            "Allocated sum incorrect"
        )


@receiver(post_save, sender=SponsorForStudent)
def save(instance, created, *args, **kwargs):
    if created:
        instance.student_sponsor.spent_sum = int(instance.student_sponsor.spent_sum) + int(instance.sponsor_allocated_sum)
        instance.student_sponsor.save()

        instance.student.allocated_sum = int(instance.student.allocated_sum) + int(instance.sponsor_allocated_sum)
        instance.student.save()
