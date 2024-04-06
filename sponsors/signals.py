from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from sponsors.models import Sponsor


# @receiver(post_save, sender=Sponsor)
# def create(sender, instance, **kwargs):
#     allocated_sum = instance.student_sponsor.filter(student_sponsor=instance)
#     if allocated_sum:
#         allocated_sum = allocated_sum.sponsor_allocated_sum
#         if instance.sponsorship_sum != allocated_sum:
#             instance.sponsorship_sum = int(instance.sponsorship_sum) - int(allocated_sum)
#             instance.save(update_fields=['sponsorship_sum'])
#
#     # if instance.pk:
#     #     old_instance = Sponsor.objects.get(pk=instance.pk)
#     #     if old_instance.sponsorship_sum != instance.sponsorship_sum:
#     #         allocated_sum = instance.student_sponsor.filter(student_sponsor=instance).get('sponsor_allocated_sum')
#     #         instance.sponsorship_sum = int(instance.sponsorship_sum) - int(allocated_sum)


@receiver(post_save, sender=Sponsor)
def update_sponsorship_sum(sender, instance, **kwargs):
    allocated_sum = instance.student_sponsor.filter(student_sponsor=instance)
    if allocated_sum:
        allocated_sum = allocated_sum.sponsor_allocated_sum
        if instance.sponsorship_sum != allocated_sum:
            instance.sponsorship_sum = int(instance.sponsorship_sum) - int(allocated_sum)
            instance.save(update_fields=['sponsorship_sum'])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

