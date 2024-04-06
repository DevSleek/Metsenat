from django.db import models
from django.core.exceptions import ValidationError

from sponsors.choices import Status, Sponsor_type
from students.models import Student
from utility.models import BaseModel


class Sponsor(BaseModel):
    fullname = models.CharField(max_length=128)
    phobe_number = models.CharField(max_length=16)

    sponsorship_sum = models.CharField(max_length=16)

    type = models.CharField(max_length=16, choices=Sponsor_type.choices, default=Sponsor_type.PHYICAL_PERSON)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW)

    date = models.DateField(auto_now_add=True)

    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsor')

    def __str__(self):
        return self.fullname

    # def clean(self):
    #     if int(self.student_sponsor.get('sponsor_allocated_sum')) >= int(self.sponsorship_sum):
    #         raise ValidationError(
    #             {
    #                 'sponsorship_sum': 'Sponsor\'s spent sum must be less than or equal to sponsorship sum',
    #             }
    #         )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    