from django.contrib import admin

from accounts.models import Lead

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lead, AuthorAdmin)