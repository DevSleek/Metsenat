from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError

from students.choices import Student_type
from utility.models import BaseModel


class Student(BaseModel):
    fullname = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)

    contract_sum = models.CharField(max_length=16)
    allocated_sum = models.CharField(max_length=16, default=0)

    type = models.CharField(max_length=16, choices=Student_type.choices, default=Student_type.BACHELOR)

    otm = models.ForeignKey('OTM', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.fullname


class OTM(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SponsorForStudent(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsored_student')
    student_sponsor = models.ForeignKey('sponsors.Sponsor', on_delete=models.CASCADE, related_name='student_sponsor')
    sponsor_allocated_sum = models.CharField(max_length=16)

    def clean(self):
        total_allocated_sum = SponsorForStudent.objects.filter(student=self.student).aggregate(total_allocated_sum=Sum('sponsor_allocated_sum'))['total_allocated_sum'] or 0
        if int(total_allocated_sum) >= int(self.student.contract_sum):
            raise ValidationError(
                {
                    'sponsor_allocated_sum': 'Sponsors\' allocated sum must be less than or equal to student\'s contract sum '
                                             '|| The sponsor has no sponsorship money left or has too much allocated money',
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student_sponsor.fullname} for {self.student.fullname}'

