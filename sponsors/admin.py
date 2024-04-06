from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phobe_number', 'students', 'sponsorship_sum', 'type', 'status', 'date']


admin.site.register(Sponsor, SponsorAdmin)
