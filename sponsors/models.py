from django.db import models
from django.core.exceptions import ValidationError

from sponsors.choices import Status, Sponsor_type
from students.models import Student
from utility.models import BaseModel


class Sponsor(BaseModel):
    fullname = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)

    sponsorship_sum = models.CharField(max_length=16)
    spent_sum = models.CharField(max_length=16, default=0)

    type = models.CharField(max_length=16, choices=Sponsor_type.choices, default=Sponsor_type.PHYICAL_PERSON)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname


    