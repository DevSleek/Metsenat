from django.utils.dateparse import parse_date
from rest_framework import filters


class DateRangeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_date_param = request.query_params.get('start_date', None)
        end_date_param = request.query_params.get('end_date', None)

        if start_date_param and end_date_param:
            try:
                start_date = parse_date(start_date_param)
                end_date = parse_date(end_date_param)
                # Custom filtering logic using start_date and end_date
                queryset = queryset.filter(created_at__range=(start_date, end_date))
            except ValueError:
                # Handle invalid date format
                pass
        return queryset
