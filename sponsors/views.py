from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from sponsors.models import Sponsor
from sponsors.serializers import SponsorSerializer
from sponsors.filters import DateRangeFilterBackend


class SponsorListAPIView(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, DateRangeFilterBackend]
    search_fields = ['fullname', ]
    filterset_fields = ['status', 'sponsorship_sum', ]
