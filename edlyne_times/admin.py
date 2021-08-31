from django.contrib import admin

from edlyne_times.models import report
from edlyne_times.models import Tsx_losers
from edlyne_times.models import Post

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(report,AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class Tsx_losersAdmin(admin.ModelAdmin):
    list_display = ('name', 'change')

admin.site.register(Tsx_losers, Tsx_losersAdmin)
