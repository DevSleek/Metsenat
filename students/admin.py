from django.contrib import admin

from students.models import Student, SponsorForStudent, OTM


class StudentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone_number', 'otm', 'contract_sum', 'allocated_sum', 'type']


admin.site.register(Student, StudentAdmin)


class SponsorForStudentAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_sponsor', 'sponsor_allocated_sum']


admin.site.register(SponsorForStudent, SponsorForStudentAdmin)


class OTMAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(OTM, OTMAdmin)