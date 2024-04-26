from rest_framework import serializers

from students.models import Student, OTM, SponsorForStudent


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['fullname', 'type', 'otm', 'allocated_sum', 'contract_sum']