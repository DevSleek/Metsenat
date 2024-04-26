from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone_number', 'sponsorship_sum', 'spent_sum', 'type', 'status', 'date']


admin.site.register(Sponsor, SponsorAdmin)
