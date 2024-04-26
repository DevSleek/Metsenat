from rest_framework import serializers

from sponsors.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ['fullname', 'phone_number', 'sponsorship_sum', 'spent_sum', 'created_at', 'status']