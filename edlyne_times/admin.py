from django.contrib import admin

from edlyne_times.models import report

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(report, AuthorAdmin)
